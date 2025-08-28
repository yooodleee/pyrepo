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
    result = []
    tasks = range(30)
    start = time.time()
    pool = mp.Pool(processes=4)
    iterator = pool.imap(foo, tasks)
    while True:
        try:
            result.append(next(iterator))
        except StopIteration:
            break
        except Exception as e:
            result.append(e)
    end = time.time()
    print(f'result - {result}')
    print(f'총 걸린 시간 - {end - start}')

"""
Process SpawnPoolWorker-1 started working on task 0
Process SpawnPoolWorker-1 started working on task 1
Process SpawnPoolWorker-2 started working on task 2
Process SpawnPoolWorker-3 started working on task 3
Process SpawnPoolWorker-4 started working on task 4
Process SpawnPoolWorker-1 ended working on task 1
Process SpawnPoolWorker-1 started working on task 5
Process SpawnPoolWorker-4 ended working on task 4
Process SpawnPoolWorker-2 ended working on task 2
Process SpawnPoolWorker-3 ended working on task 3
Process SpawnPoolWorker-2 started working on task 7
Process SpawnPoolWorker-4 started working on task 6
Process SpawnPoolWorker-3 started working on task 8
Process SpawnPoolWorker-1 ended working on task 5
Process SpawnPoolWorker-1 started working on task 9
Process SpawnPoolWorker-2 ended working on task 7
Process SpawnPoolWorker-4 ended working on task 6
Process SpawnPoolWorker-4 started working on task 11
Process SpawnPoolWorker-2 started working on task 10
Process SpawnPoolWorker-3 ended working on task 8
Process SpawnPoolWorker-3 started working on task 12
Process SpawnPoolWorker-1 ended working on task 9
Process SpawnPoolWorker-1 started working on task 13
Process SpawnPoolWorker-3 ended working on task 12
Process SpawnPoolWorker-3 started working on task 14
Process SpawnPoolWorker-4 ended working on task 11
Process SpawnPoolWorker-4 started working on task 15
Process SpawnPoolWorker-2 ended working on task 10
Process SpawnPoolWorker-2 started working on task 16
Process SpawnPoolWorker-1 ended working on task 13
Process SpawnPoolWorker-1 started working on task 17
Process SpawnPoolWorker-2 ended working on task 16
Process SpawnPoolWorker-3 ended working on task 14
Process SpawnPoolWorker-4 ended working on task 15
Process SpawnPoolWorker-2 started working on task 18
Process SpawnPoolWorker-4 started working on task 20
Process SpawnPoolWorker-3 started working on task 19
Process SpawnPoolWorker-1 ended working on task 17
Process SpawnPoolWorker-1 started working on task 21
Process SpawnPoolWorker-4 ended working on task 20
Process SpawnPoolWorker-3 ended working on task 19
Process SpawnPoolWorker-2 ended working on task 18
Process SpawnPoolWorker-3 started working on task 23
Process SpawnPoolWorker-4 started working on task 22
Process SpawnPoolWorker-2 started working on task 24
Process SpawnPoolWorker-1 ended working on task 21
Process SpawnPoolWorker-1 started working on task 25
Process SpawnPoolWorker-4 ended working on task 22
Process SpawnPoolWorker-2 ended working on task 24
Process SpawnPoolWorker-3 ended working on task 23
Process SpawnPoolWorker-4 started working on task 26
Process SpawnPoolWorker-2 started working on task 27
Process SpawnPoolWorker-3 started working on task 28
Process SpawnPoolWorker-1 ended working on task 25
Process SpawnPoolWorker-1 started working on task 29
Process SpawnPoolWorker-3 ended working on task 28
Process SpawnPoolWorker-4 ended working on task 26
Process SpawnPoolWorker-2 ended working on task 27
Process SpawnPoolWorker-1 ended working on task 29
result - [ZeroDivisionError('division by zero'), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
총 걸린 시간 - 8.163708448410034
"""