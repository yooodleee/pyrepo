"""
Pool.map()은 모든 작업을 한 번에 Pool에 넘기고 넘긴 작업이 완료된 후에만 결과를 순서대로 처리함.
"""

import time
import multiprocessing as mp


def foo(n):
    print(f'Process {mp.current_process().name} started working on task {n}', flush=True)
    if n == 0: # ZeroDivisionError: division by zero 
        1 / 0
    time.sleep(1)
    print(f'Process {mp.current_process().name} ended working on task {n}', flush=True)

    return n


if __name__ == "__main__":
    start = time.time()
    tasks = range(30)
    pool = mp.Pool(processes=4)
    pool.map(foo, tasks) 
    pool.close()
    pool.join()
    end = time.time()
    print(f'총 걸린 시간 - {end - start}')

    