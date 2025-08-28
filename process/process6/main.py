from multiprocessing import Pool
import multiprocessing as mp
import time
import os


def func(num):
    c_proc = mp.current_process()
    print("Running on Process", c_proc.name, "PID", c_proc.pid)
    time.sleep(1)
    print("Ended", num, "Process", c_proc.name)

    return num


if __name__ == "__main__":
    p = Pool(4)
    start = time.time()

    ret = p.apply(func, (1, ))
    print(ret)
    ret = p.apply(func, (2, ))
    print(ret)
    ret = p.apply(func, (3, ))
    print(ret)
    ret = p.apply(func, (4, ))
    print(ret)
    ret = p.apply(func, (5, ))
    print(ret)

    delta_t = time.time() - start
    print("Time: ", delta_t)

    p.close()
    p.join()


"""
Running on Process SpawnPoolWorker-1 PID 18496
Ended 1 Process SpawnPoolWorker-1
1
Running on Process SpawnPoolWorker-2 PID 26508
Ended 2 Process SpawnPoolWorker-2
2
Running on Process SpawnPoolWorker-3 PID 35524
Ended 3 Process SpawnPoolWorker-3
3
Running on Process SpawnPoolWorker-4 PID 31880
Ended 4 Process SpawnPoolWorker-4
4
Running on Process SpawnPoolWorker-1 PID 18496
Ended 5 Process SpawnPoolWorker-1
5
Time:  5.089715003967285
"""