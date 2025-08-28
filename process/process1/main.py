from multiprocessing import Pool
import time
import os


def power_task(x):
    print(f"Process {os.getpid()} is processing {x}")
    time.sleep(1) 
    return x ** 2


def multiply_task(a, b):
    return a * b


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    with Pool(processes=3) as pool:
        # 1) map: 리스트 요소 병렬 처리 
        results = pool.map(power_task, data)
        print("\nmap results:", results)

        # 2) apply_async: 비동기 실행(Future 객체 반환)
        async_result = pool.apply_async(power_task, (10,))
        print("apply_async result:", async_result.get()) # .get()으로 결과 회수

        # 3) starmap: 여러 인자를 튜플로 전달 
        pairs = [(2, 3), (4, 5), (6, 7)]
        starmap_results = pool.starmap(multiply_task, pairs)
        print("starmap results:", starmap_results)

        # 4) imap: iterator로 결과 받기(메모리 절약)
        for r in pool.imap(power_task, range(6, 10)):
            print("imap result:", r)

"""
Process 33392 is processing 1
Process 6384 is processing 2
Process 13144 is processing 3
Process 33392 is processing 4
Process 6384 is processing 5

map results: [1, 4, 9, 16, 25]
Process 13144 is processing 10
apply_async result: 100
starmap results: [6, 20, 42]
Process 33392 is processing 6
Process 6384 is processing 7
Process 13144 is processing 8
Process 33392 is processing 9
imap result: 36
imap result: 49
imap result: 64
imap result: 81
"""