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

    ret1 = p.apply_async(func, (1, ))
    ret2 = p.apply_async(func, (2, ))
    ret3 = p.apply_async(func, (3, ))
    ret4 = p.apply_async(func, (4, ))
    ret5 = p.apply_async(func, (5, ))
    print(ret1.get(), ret2.get(), ret3.get(), ret4.get(), ret5.get())

    print(f'execution time: {time.time() - start}')

    p.close()
    p.join()

# # Output:
# 1 2 3 4 5
# execution time: 2.0463151931762695
# Running on Process: SpawnPoolWorker-3, PID: 17112
# Ended: 3, Processes: SpawnPoolWorker-3
# Running on Process: SpawnPoolWorker-1, PID: 1596
# Ended: 1, Processes: SpawnPoolWorker-1
# Running on Process: SpawnPoolWorker-4, PID: 14840
# Ended: 4, Processes: SpawnPoolWorker-4
# Running on Process: SpawnPoolWorker-2, PID: 12284
# Ended: 2, Processes: SpawnPoolWorker-2
# Running on Process: SpawnPoolWorker-2, PID: 12284
# Ended: 5, Processes: SpawnPoolWorker-2
