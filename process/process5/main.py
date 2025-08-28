"""
Pool.imap_unordered(): 작업을 하나씩 실행하고, 사용 가능한 순서대로 작업 결과를 처리함.
    빨리 끝나는 순서대로 처리해서 넘겨줌.
"""
import time
import multiprocessing as mp


def foo(n):
    print(f'Process {mp.current_process().name} started working on task {n}', flush=True)
    if n == 0: 
        1 / 0
    time.sleep(n % 2)

    return n


if __name__ == "__main__":
    result = []
    tasks = range(30)
    start = time.time()
    pool = mp.Pool(processes=4)
    iterator = pool.imap_unordered(foo, tasks) # Pool.imap()과 비교 해보세요.
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
Process SpawnPoolWorker-2 started working on task 3
Process SpawnPoolWorker-3 started working on task 4
Process SpawnPoolWorker-3 started working on task 5
Process SpawnPoolWorker-4 started working on task 6
Process SpawnPoolWorker-4 started working on task 7
Process SpawnPoolWorker-3 started working on task 8
Process SpawnPoolWorker-2 started working on task 9
Process SpawnPoolWorker-1 started working on task 10
Process SpawnPoolWorker-3 started working on task 11
Process SpawnPoolWorker-1 started working on task 12
Process SpawnPoolWorker-1 started working on task 13
Process SpawnPoolWorker-4 started working on task 14
Process SpawnPoolWorker-4 started working on task 15
Process SpawnPoolWorker-1 started working on task 16
Process SpawnPoolWorker-3 started working on task 17
Process SpawnPoolWorker-2 started working on task 18
Process SpawnPoolWorker-1 started working on task 19
Process SpawnPoolWorker-2 started working on task 20
Process SpawnPoolWorker-2 started working on task 21
Process SpawnPoolWorker-4 started working on task 22
Process SpawnPoolWorker-4 started working on task 23
Process SpawnPoolWorker-2 started working on task 24
Process SpawnPoolWorker-3 started working on task 25
Process SpawnPoolWorker-1 started working on task 26
Process SpawnPoolWorker-2 started working on task 27
Process SpawnPoolWorker-1 started working on task 28
Process SpawnPoolWorker-1 started working on task 29
result - [ZeroDivisionError('division by zero'), 2, 4, 6, 5, 3, 1, 8, 10, 12, 7, 14, 13, 11, 9, 16, 18, 20, 15, 22, 21, 17, 19, 24, 26, 28, 23, 25, 27, 29]
총 걸린 시간 - 4.1340248584747314
"""