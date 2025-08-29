from multiprocessing import Process, Pipe, current_process
import time
import os


def worker(id, baseNum, conn):
		process_id = os.getpid()
		process_name = current_process().name
		
		sub_total = 0
		for i in range(baseNum):
				sub_total += 1
		
		# Produce
		conn.send(sub_total) # child가 send로 보내면
		conn.close() # pipeline 잠그기
		
		# 정보 출력
		print(f'Process ID: {process_id} Process Name: {process_name}')
		print(f'Result is: {sub_total}')


def main():
		parent_process_id = os.getpid()
		print(f'Parent process ID: {parent_process_id}')
		
		# 성능 측정을 위한 시작 시간 기록
		start_time = time.time()
		
		# Pipe 선언
		parent_conn, child_conn = Pipe()
		
		p = Process(name='child', target=worker, args=('child', 10000, child_conn))
		p.start()
		p.join()
		
		# 순수 계산 시간
		print("---- %s seconds ----" % (time.time() - start_time))
		
		print('Main-Processing Total Count: {}'.format(parent_conn.recv())) # parent가 receive합니다.
		print("Multi process is Done!")
		

if __name__ == "__main__":
		main()

"""
Parent process ID: 21664
Process ID: 34300 Process Name: child
Result is: 10000
---- 0.07211732864379883 seconds ----
Main-Processing Total Count: 10000
Multi process is Done!
"""