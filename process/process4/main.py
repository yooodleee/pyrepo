"""
Pool.imap()은 작업을 하나씩 실행하고, 사용 가능한 순서대로 결과를 처리합니다.
"""
import time 
import multiprocessing as mp


def foo(n):
    print(f'Process {mp.current_process().name} started working on task {n}', flush=True)
    if n == 0:
        1 / 0
    time.sleep(1)
    print(f'Process {mp.current_process().name} ended working on task {n}', flush=True)

    return n


if __name__ == "__main__":
    tasks = range(30)
    start = time.time()
    pool = mp.Pool(processes=4)
    result = list(pool.imap(foo, tasks))
    end = time.time()
    print(f'총 걸린 시간 - {end - start}')

"""
Process SpawnPoolWorker-1 started working on task 0
Process SpawnPoolWorker-1 started working on task 1
multiprocessing.pool.RemoteTraceback:
    ZeroDivisionError: division by zero
"""