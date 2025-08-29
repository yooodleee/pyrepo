import multiprocessing as mp
import queue
import time


def create_work(work_queue, workload=0):
    for _ in range(100):
        workload += 1
        work_queue.put(workload)

def finish_work(work_queue):
    while True:
        try:
            workload = work_queue.get(False) # non-blocking을 위함
            workload -= 1
        except queue.Empty:
            break
    print(f"Consumed: {workload}")


if __name__ == "__main__":
    # Process를 선언하는 code가 main에 있어야 합니다.
    workloads = [100, 200]
    work_queue = mp.Queue()
    procs = []

    # producer process 선언
    for work in workloads:
        producer_proc = mp.Process(target=create_work, args=(work_queue, work))
        procs.append(producer_proc)
        producer_proc.start()
    
    # producer process 선언
    consumer_proc = mp.Process(target=finish_work, args=(work_queue, ))
    procs.append(consumer_proc)
    consumer_proc.start()

    for proc in procs:
        proc.join()

"""
Consumed: 299
"""