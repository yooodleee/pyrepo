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

    # ret = p.apply_asyunc(func, (n, )).get()은 전혀 다른 의미를 가집니다.
    ret1 = p.apply_async(func, (1, ))
    ret2 = p.apply_async(func, (2, ))
    ret3 = p.apply_async(func, (3, ))
    ret4 = p.apply_async(func, (4, ))
    ret5 = p.apply_async(func, (5, ))
    print(ret1.get(), ret2.get(), ret3.get(), ret4.get(), ret5.get())

    delta_t = time.time() - start
    print("Time: ", delta_t)

    p.close()
    p.join()


"""
Running on Process SpawnPoolWorker-1 PID 34080
Running on Process SpawnPoolWorker-2 PID 29516
Running on Process SpawnPoolWorker-3 PID 4732
Running on Process SpawnPoolWorker-4 PID 13116
Ended 1 Process SpawnPoolWorker-1
Running on Process SpawnPoolWorker-1 PID 34080
Ended 3 Process SpawnPoolWorker-3
Ended 2 Process SpawnPoolWorker-2
Ended 4 Process SpawnPoolWorker-4
Ended 5 Process SpawnPoolWorker-1
1 2 3 4 5
Time:  2.0685713291168213
"""