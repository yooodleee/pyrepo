from multiprocessing import Pool
import multiprocessing as mp
import time 
import os 


def mul(x, y):
    c_proc = mp.current_process()
    print(f"Running on Process: {c_proc.name}, PID: {c_proc.pid}")
    time.sleep(1)
    print(f"Ended: {x} * {y}, Process: {c_proc.name}")

    return x * y

if __name__ == "__main__":
    p = Pool(4)
    start = time.time()

    ret = p.starmap(mul, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    print(ret)

    print(f"execution time: {time.time() - start}")

    p.close()
    p.join()

# # Output:
# [2, 6, 12, 20, 30]
# execution time: 2.0615177154541016
# Running on Process: SpawnPoolWorker-3, PID: 6488
# Ended: 3 * 4, Process: SpawnPoolWorker-3
# Running on Process: SpawnPoolWorker-4, PID: 19772
# Ended: 4 * 5, Process: SpawnPoolWorker-4
# Running on Process: SpawnPoolWorker-2, PID: 27296
# Ended: 2 * 3, Process: SpawnPoolWorker-2
# Running on Process: SpawnPoolWorker-1, PID: 28084
# Ended: 1 * 2, Process: SpawnPoolWorker-1
# Running on Process: SpawnPoolWorker-1, PID: 28084
# Ended: 5 * 6, Process: SpawnPoolWorker-1
