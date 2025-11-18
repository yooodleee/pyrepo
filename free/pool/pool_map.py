import time 
import multiprocessing as mp


def func(n):
    print(f'Process {mp.current_process().name} started working on task {n}', flush=True)
    if n == 0:
        1 / 0   # ZeroDivisionError
    time.sleep(1)
    print(f'Process {mp.current_process().name} ended working on task {n}', flush=True)

    return n

if __name__ == "__main__":
    start = time.time()
    tasks = range(30)
    pool = mp.Pool(processes=4)
    pool.map(func, tasks)
    pool.close()
    pool.join()
    print(f'execution time: {time.time() - start}')
