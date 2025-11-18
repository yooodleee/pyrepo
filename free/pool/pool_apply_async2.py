from multiprocessing import Pool
import multiprocessing as mp
import time 
import os


def func(num):
    c_proc = mp.current_process()
    print(f"Running on Process: {c_proc.name}, PID: {c_proc.pid}")
    time.sleep(1)
    print(f"Ended: {num}, Processes: {c_proc.name}")
    return num

if __name__ == "__main__":
    p = Pool(4)
    start = time.time()

    ret1 = p.apply_async(func, (1, )).get()
    ret2 = p.apply_async(func, (2, )).get()
    ret3 = p.apply_async(func, (3, )).get()
    ret4 = p.apply_async(func, (4, )).get()
    ret5 = p.apply_async(func, (5, )).get()
    print(ret1, ret2, ret3, ret4, ret5)

    print(f'execution time: {time.time() - start}')

    p.close()
    p.join()

# # Output:
# 1 2 3 4 5
# execution time: 5.066127061843872
# Running on Process: SpawnPoolWorker-2, PID: 30776
# Ended: 2, Processes: SpawnPoolWorker-2
# Running on Process: SpawnPoolWorker-3, PID: 27952
# Ended: 3, Processes: SpawnPoolWorker-3
# Running on Process: SpawnPoolWorker-4, PID: 3056
# Ended: 4, Processes: SpawnPoolWorker-4
# Running on Process: SpawnPoolWorker-1, PID: 26300
# Ended: 1, Processes: SpawnPoolWorker-1
# Running on Process: SpawnPoolWorker-1, PID: 26300
# Ended: 5, Processes: SpawnPoolWorker-1
