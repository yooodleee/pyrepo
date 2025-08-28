import time 
import multiprocessing as mp


def foo(n):
    print(f'Process {mp.current_process().name} started working on task {n}', flush=True)
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


"""
Process SpawnPoolWorker-1 started working on task 0
Process SpawnPoolWorker-2 started working on task 2
Process SpawnPoolWorker-3 started working on task 4
Process SpawnPoolWorker-4 started working on task 6
Process SpawnPoolWorker-1 ended working on task 0
Process SpawnPoolWorker-1 started working on task 1
Process SpawnPoolWorker-3 ended working on task 4
Process SpawnPoolWorker-3 started working on task 5
Process SpawnPoolWorker-2 ended working on task 2
Process SpawnPoolWorker-2 started working on task 3
Process SpawnPoolWorker-4 ended working on task 6
Process SpawnPoolWorker-4 started working on task 7
Process SpawnPoolWorker-1 ended working on task 1
Process SpawnPoolWorker-1 started working on task 8
Process SpawnPoolWorker-2 ended working on task 3
Process SpawnPoolWorker-2 started working on task 10
Process SpawnPoolWorker-3 ended working on task 5
Process SpawnPoolWorker-3 started working on task 12
Process SpawnPoolWorker-4 ended working on task 7
Process SpawnPoolWorker-4 started working on task 14
Process SpawnPoolWorker-1 ended working on task 8
Process SpawnPoolWorker-1 started working on task 9
Process SpawnPoolWorker-2 ended working on task 10
Process SpawnPoolWorker-2 started working on task 11
Process SpawnPoolWorker-4 ended working on task 14
Process SpawnPoolWorker-4 started working on task 15
Process SpawnPoolWorker-3 ended working on task 12
Process SpawnPoolWorker-3 started working on task 13
Process SpawnPoolWorker-1 ended working on task 9
Process SpawnPoolWorker-1 started working on task 16
Process SpawnPoolWorker-2 ended working on task 11
Process SpawnPoolWorker-2 started working on task 18
Process SpawnPoolWorker-3 ended working on task 13
Process SpawnPoolWorker-3 started working on task 20
Process SpawnPoolWorker-4 ended working on task 15
Process SpawnPoolWorker-4 started working on task 22
Process SpawnPoolWorker-1 ended working on task 16
Process SpawnPoolWorker-1 started working on task 17
Process SpawnPoolWorker-4 ended working on task 22
Process SpawnPoolWorker-4 started working on task 23
Process SpawnPoolWorker-2 ended working on task 18
Process SpawnPoolWorker-2 started working on task 19
Process SpawnPoolWorker-3 ended working on task 20
Process SpawnPoolWorker-3 started working on task 21
Process SpawnPoolWorker-1 ended working on task 17
Process SpawnPoolWorker-1 started working on task 24
Process SpawnPoolWorker-2 ended working on task 19
Process SpawnPoolWorker-3 ended working on task 21
Process SpawnPoolWorker-2 started working on task 26
Process SpawnPoolWorker-3 started working on task 28
Process SpawnPoolWorker-4 ended working on task 23
Process SpawnPoolWorker-1 ended working on task 24
Process SpawnPoolWorker-1 started working on task 25
Process SpawnPoolWorker-3 ended working on task 28
Process SpawnPoolWorker-2 ended working on task 26
Process SpawnPoolWorker-3 started working on task 29
Process SpawnPoolWorker-2 started working on task 27
Process SpawnPoolWorker-1 ended working on task 25
Process SpawnPoolWorker-2 ended working on task 27
Process SpawnPoolWorker-3 ended working on task 29
총 걸린 시간 - 8.132371425628662
"""