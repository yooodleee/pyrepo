from multiprocessing import Pool
import multiprocessing as mp
import time 
import os


def func(num):
    c_proc = mp.current_process()
    print(f"Running on Process: {c_proc.name}, PID: {c_proc.pid}")
    time.sleep(1)
    print(f"Ended: {num}, Process: {c_proc.name}")
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

    print(f'execution time: {time.time() - start}')

    p.close()
    p.join()

# Output:
# 1
# 2
# 3
# 4
# 5
# execution time: 5.069920539855957
# Running on Process: SpawnPoolWorker-2, PID: 30212
# Ended: 2, Process: SpawnPoolWorker-2
# Running on Process: SpawnPoolWorker-3, PID: 11112
# Ended: 3, Process: SpawnPoolWorker-3
# Running on Process: SpawnPoolWorker-4, PID: 8212
# Ended: 4, Process: SpawnPoolWorker-4
# Running on Process: SpawnPoolWorker-1, PID: 31716
# Ended: 1, Process: SpawnPoolWorker-1
# Running on Process: SpawnPoolWorker-1, PID: 31716
# Ended: 5, Process: SpawnPoolWorker-1
