import time 
import multiprocessing as mp


def func(n):
    print(f'Process {mp.current_process().name} started working on task {n}', flush=True)
    if n == 0:
        1 / 0   # ZeroDivisionError
    time.sleep(n % 2)
    print(f'Process {mp.current_process().name} ended working on task {n}', flush=True)

    return n

if __name__ == "__main__":
    result = []
    tasks = range(30)
    start = time.time()
    pool = mp.Pool(processes=4)
    iterator = pool.imap_unordered(func, tasks)

    while True:
        try:
            result.append(next(iterator))
        except StopIteration:
            break
        except Exception as e:
            result.append(e)
    
    print(f'result - {result}')
    print(f'execution time: {time.time() - start}')

# # Output: 
# result - [ZeroDivisionError('division by zero'), 2, 4, 6, 3, 8, 1, 10, 5, 12, 7, 14, 9, 16, 11, 18, 13, 20, 15, 22, 19, 24, 17, 26, 21, 28, 23, 27, 25, 29]
# execution time: 4.108430862426758