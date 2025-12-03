import argparse
import numpy as np
import os
import cv2
import gym
import tensorflow as tf
from tensorflow.python import keras
import tf_slim as slim
from tensorpack import *

from atar_wrapper import FireRestEnv, FrameStack, LimitLength, MapState
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
        
        with slim.arg_scope(keras.layers.Conv2D)