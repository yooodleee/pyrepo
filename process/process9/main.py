from multiprocessing import Process, Queue, current_process
import time
import os


def worker(id, baseNum, q):
		process_id = os.getpid()
		process_name = current_process().name
		
		sub_total = 0
		for i in range(baseNum):
				sub_total += 1
		
		# Produce
		q.put(sub_total)
		# 정보 출력
		print(f'Process ID: {process_id} Process Name: {process_name}')
		print(f'Result is: {sub_total}')


def main():
		parent_process_id = os.getpid()
		print(f'Parent process ID: {parent_process_id}')
		
		processes = list()
		
		# 성능 측정을 위한 시작 시간 기록
		start_time = time.time()
		
		# Queue 선언
		q = Queue()
		for i in range(5):
				p = Process(name=str(i), target=worker, args=(i, 10000, q))
				
				processes.append(p)
				p.start()
		
		for process in processes:
				process.join()
		
		# 순수 계산 시간
		print("---- %s seconds ----" % (time.time() - start_time))
		
		# 종료 플래그
		q.put('exit')
		total = 0
		while True:
				tmp = q.get()
				if tmp == 'exit':
						break
				else:
						total += tmp
		
		print(f'Main-Processing Total Count: {total}')
		print("Multi process is Done!")


if __name__ == "__main__":
		main()


"""
Parent process ID: 25024
Process ID: 26556 Process Name: 0
Result is: 10000
Process ID: 12172 Process Name: 1
Result is: 10000
Process ID: 10212 Process Name: 2
Result is: 10000
Process ID: 28704 Process Name: 3
Result is: 10000
Process ID: 17028 Process Name: 4
Result is: 10000
---- 0.1217350959777832 seconds ----
Main-Processing Total Count: 50000
Multi process is Done!
"""