from multiprocessing import Process
import time
import logging


def main():
		# Logging format 설정
		form = "%(asctime)s: %(message)s"
		logging.basicConfig(format=form, level=logging.INFO, datefmt="%H:%M:%S")
		
		# 함수 인자 확인
		p = Process(target=process_function, args=('First', ))
		logging.info("Main-Process: before creating Process")
		
		# 프로세스 시작
		p.start()
		logging.info("Main-Process: During Process...")
		
		# 프로세스 종료될 때까지 대기
		logging.info("Main-Process: Joined Process")
		p.join()
		
		# 프로세스 상태 확인
		print(f'Process p is alive: {p.is_alive()}')


# multiprocess로 실행할 함수
def process_function(name):
		print("This is Sub-Process {}: starting".format(name))
		time.sleep(3) # 3 초간 쉬어주고
		print("This is Sub-Process {}: finishing".format(name))

if __name__ == '__main__':
		main()


"""
19:19:19: Main-Process: before creating Process
19:19:19: Main-Process: During Process...
19:19:19: Main-Process: Joined Process
This is Sub-Process First: starting
This is Sub-Process First: finishing
Process p is alive: False
"""