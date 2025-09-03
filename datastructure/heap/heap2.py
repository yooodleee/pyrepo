import heapq


def solution(L, T):
	"""주어진 리스트를 힙 구조로 변환"""
	heapq.heapify(L)
		
	result = 0
		
	while len(L) >= 2: # IndexError 방지
		"""힙에서 최솟값을 가져옵니다."""
		min_ = heapq.heappop(L)
		if min_ >= T: # 최솟값이 T보다 크다는 조건 만족(종료)
			print("-" * 40, "\nresult:", result)
			return result
				
		else: # 두 번째로 작은 값을 가져와서 합친 값을 힙에 삽입합니다.
			min_2 = heapq.heappop(L)
			heapq.heappush(L, min_ + min_2)
			result += 1
			print("step{}: [{}, {}] 합침".format(result, min_, min_2))
			print("       ->", L)
		

	if L[0] > T:
		print("-" * 40, "\nresult:", result)
		return result
	else:
		print("-" * 40, "\nMission Failed")
		return -1