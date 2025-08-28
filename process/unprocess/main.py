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
    result = []
    for task in tasks:
        foo(task)
    end = time.time()
    print(f'총 걸린 시간 - {end - start}')

"""
Process MainProcess started working on task 0
Process MainProcess ended working on task 0
Process MainProcess started working on task 1
Process MainProcess ended working on task 1
Process MainProcess started working on task 2
Process MainProcess ended working on task 2
Process MainProcess started working on task 3
Process MainProcess ended working on task 3
Process MainProcess started working on task 4
Process MainProcess ended working on task 4
Process MainProcess started working on task 5
Process MainProcess ended working on task 5
Process MainProcess started working on task 6
Process MainProcess ended working on task 6
Process MainProcess started working on task 7
Process MainProcess ended working on task 7
Process MainProcess started working on task 8
Process MainProcess ended working on task 8
Process MainProcess started working on task 9
Process MainProcess ended working on task 9
Process MainProcess started working on task 10
Process MainProcess ended working on task 10
Process MainProcess started working on task 11
Process MainProcess ended working on task 11
Process MainProcess started working on task 12
Process MainProcess ended working on task 12
Process MainProcess started working on task 13
Process MainProcess ended working on task 13
Process MainProcess started working on task 14
Process MainProcess ended working on task 14
Process MainProcess started working on task 15
Process MainProcess ended working on task 15
Process MainProcess started working on task 16
Process MainProcess ended working on task 16
Process MainProcess started working on task 17
Process MainProcess ended working on task 17
Process MainProcess started working on task 18
Process MainProcess ended working on task 18
Process MainProcess started working on task 19
Process MainProcess ended working on task 19
Process MainProcess started working on task 20
Process MainProcess ended working on task 20
Process MainProcess started working on task 21
Process MainProcess ended working on task 21
Process MainProcess started working on task 22
Process MainProcess ended working on task 22
Process MainProcess started working on task 23
Process MainProcess ended working on task 23
Process MainProcess started working on task 24
Process MainProcess ended working on task 24
Process MainProcess started working on task 25
Process MainProcess ended working on task 25
Process MainProcess started working on task 26
Process MainProcess ended working on task 26
Process MainProcess started working on task 27
Process MainProcess ended working on task 27
Process MainProcess started working on task 28
Process MainProcess ended working on task 28
Process MainProcess started working on task 29
Process MainProcess ended working on task 29
총 걸린 시간 - 30.105390071868896
"""