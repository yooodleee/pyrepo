import os
import threading
import time
from concurrent.futures import ProcessPoolExecutor


def calculate(n):
    print(f"{os.getpid()} process | {threading.get_ident()} thread | n: {n}")
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += i * j * k
    return total

def main(nums):
    with ProcessPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(calculate, nums))
        print(results)

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()

    start = time.time()
    main([300] * 10)
    print("elapsed-time: ", time.time() - start)