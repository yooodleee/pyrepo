import multiprocessing as mp
import time


def create_work(work_queue, workload=0):
    for _ in range(100):
        workload += 1
        work_queue.put(workload)

def finish_work(work_queue):
    while not work_queue.empty():
        workload = work_queue.get(False) # non-blocking을 위함
        workload -= 1


if __name__ == "__main__":
    # Process를 선언하는 code가 main에 있어야 합니다.
    workloads = [100, 200]
    work_queue = mp.Queue()
    procs = []

    # producer process 선언
    for work in workloads:
        producer_proc = mp.Process(target=create_work, args=(work, work_queue))
        procs.append(producer_proc)
        producer_proc.start()
    
    # producer process 선언
    consumer_proc = mp.Process(target=finish_work, args=(work_queue, ))
    procs.append(consumer_proc)
    consumer_proc.start()

    for proc in procs:
        proc.join()

"""
Process 20588 is processing 1
Process 17200 is processing 2
Process 10816 is processing 3
Process 17200 is processing 4
Process 10816 is processing 5

map results: [1, 4, 9, 16, 25]
Process 20588 is processing 10
apply_async result: 100
starmap results: [6, 20, 42]
Process 17200 is processing 6
Process 10816 is processing 7
Process 20588 is processing 8
Process 17200 is processing 9
imap result: 36
imap result: 49
imap result: 64
imap result: 81
"""