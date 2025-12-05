import argparse
import numpy as np
import os
import cv2
import gym
import tensorflow as tf
import keras                # from tensorflow.python import keras
import tf_slim as slim
from tensorpack import *

from atar_wrapper import FireRestEnv, FrameStack, LimitLength, MapState
from common import Evaluator, eval_model_multithread, play_n_episodes
from common import Model as DQNModel
from expreplay import ExReplay

BATCH_SIZE = 64
IMAGE_SIZE = (83, 84)
FRAME_HISTORY = 4
UPDATE_FREQUENCE = 4    # the number of new state transitions per parameter update (per training step)
MEMORY_SIZE = 1e6       # will consume at least 1e6 * 84 * 84 bytes == 6.6G memory
INIT_MEMORY_SIZE = MEMORY_SIZE // 20
STEPS_PER_EPOCH = 10000 // UPDATE_FREQUENCE     # each epoch if 100k state transitions
NUM_PARALLEL_PLAYERS = 3

USE_GYM = False
ENV_NAME = None


def resize_keepdims(im, size):
    """OpenCV's resize remove the extra dimension for grayscale images."""
    ret = cv2.resize(im, size)
    if im.ndim == 3 and ret.ndim == 2:
        ret = ret[:, :, np.newaxis]     # 2D (H, W) -> 3D (H, W, 1)
    return ret

def get_player(viz=False, train=False):
    if USE_GYM:
        env = gym.make(ENV_NAME, render_mode='human' if viz else None)
    else:
        from atari import AtariPlayer
        env = AtariPlayer(ENV_NAME, frmae_skip=4, viz=viz,
                          live_lost_as_eoe=train, max_num_frames=60000)
    
    env = FireRestEnv(env)
    env = MapState(env, lambda im: resize_keepdims(im, IMAGE_SIZE))
    if not train:
        # in training, history is taken care of in expreplay buffer
        env = FrameStack(env, FRAME_HISTORY)
    if train and USE_GYM:
        env = LimitLength(env, 60000)
    return env


class Model(DQNModel):
    """A DQN model for 2D/3D (image) observations."""
    def _get_DQN_prediction(self, image):
        """image: N, H, W, (C), Hist"""
        if image.shape.rank == 5:
            # merge C and Hist
            image = tf.reshape(
                image,
                [-1] + list(self.state_shape[:2]) + [self.state_shape[2] * FRAME_HISTORY]
            )
        image = image / 255.0
        
        with slim.arg_scope(keras.layers.Conv2D, 
                            activation=lambda x: keras.layers.PReLU('prelu', x),
                            use_bias=True):
            l = keras.Sequential([
                keras.layers.Conv2D('conv0', 32, 8, strides=4),
                keras.layers.Conv2D('conv1', 64, 4, strides=2),
                keras.layers.Conv2D('conv2', 64, 3),
                keras.layers.Dense('fc0', 512),                     # FullyConnected
                keras.layers.LeakyReLU(alpha=0.01),
            ])
        
        if self.method != 'Duebling':
            V = keras.layers.Dense('fct', l, 1)
            AS = keras.layers.Dense('fctA', l, self.num_actions)
            Q = tf.add(AS, V - self.reduce_mean(AS, l, keep_dims=True))
        
        return tf.identity(Q, name='QValue')


def get_config(model):
    global args 
    expreplay = ExReplay(
        predictor_io_names=(['state'], ['QValue']),
        get_player=lambda: get_player(train=True),
        num_parallel_players=NUM_PARALLEL_PLAYERS,
        state_shape=model.state_shape,
        batch_size=BATCH_SIZE,
        memory_size=MEMORY_SIZE,
        init_memory_size=INIT_MEMORY_SIZE,
        update_frequency=UPDATE_FREQUENCE,
        history_len=FRAME_HISTORY,
        state_dtype=model.state_dtype.as_numpy_dtype
    )

    return keras.callbacks(
        data=tf.data(expreplay),
        model=model,
        callback=[
            keras.callbacks.ModelCheckpoint(),
            keras.callbacks(
                tf.function(DQNModel.update_target_param, verbose=True),
                every_k_steps=5000
            ),
            expreplay,
            keras.callbacks.LearningRateScheduler(
                setattr(expreplay, 'exploration'),
                [(0, 1), (10, 0.1), (400, 0.01)],       # 1 -> 0.1 in the first million steps
                interp='linear'
            ),
            keras.callbacks(Evaluator(
                args.num_eval, ['state'], ['QValue'], get_player),
                every_k_epochs=5 if 'pong' in args.env.lower() else 10),    # eval more frequently for easy games
        ],
        steps_per_epoch=STEPS_PER_EPOCH,
        max_epoch=500,      # a total of 50M state transition
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", help="comma separated list of GPU(s) to use.")
    parser.add_argument("--load", help="load model")
    parser.add_argument("--task", help="task to perform", choices=["play", "eval", "train"], default="train")
    parser.add_argument("--env", required=True, help="either an atari rom file (that ends with .bin) or a gym atari environment name")
    parser.add_argument("--algo", help='algorithm', choices=["DQN", "Double", "Dueling"], default="Double")
    parser.add_argument("--num-eval", default=50, type=int)
    
    args = parser.parse_args()
    if args.gpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu
    ENV_NAME = args.env
    USE_GYM = not ENV_NAME.endswith('.bin')

    # set num_actions
    num_actions = get_player().action_space.n
    logger.info(f"ENV: {args.env}, Num Actions: {num_actions}")

    state_shape = IMAGE_SIZE + (3, ) if USE_GYM else IMAGE_SIZE
    model = Model(state_shape, FRAME_HISTORY, args.algo, num_actions)

    if args.task != "train":
        assert args.load is not None

        pred = model.predict(keras.Model.predict(
            model=model,
            session_init=keras.initializers.GlorotUniform(args.load),
            input_names=['state'],
            output_names=['QValue'],
        ))
    
    if args.task == "play":
        play_n_episodes(get_player(viz=0.01), pred, 100, render=True)
    elif args.task == "eval":
        eval_model_multithread(pred, args.num_eval, get_player)
    else:
        logger.set_logger_dir(
            os.path.join("train_log", f"DQN-{os.path.basename(args.env).split('.'[0])}")
        )
        config = get_config(model)
        config.session_init = keras.initializers.GlorotUniform(args.load)
        model.fit()(config, model.fit())