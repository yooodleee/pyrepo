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
    result = []
    tasks = range(30)
    start = time.time()
    pool = mp.Pool(processes=4)
    iterator = pool.imap(func, tasks)

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
# result - [ZeroDivisionError('division by zero'), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# execution time: 8.094878435134888
