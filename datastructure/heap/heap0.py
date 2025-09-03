import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)
# [10, 50, 20]


heap2 = [50, 10, 20]
heapq.heapify(heap2)

print(heap2)
# [10, 50, 20]


result = heapq.heappop(heap)
print(result)
print(heap)
# 10
# [20, 50]


result2 = heap[0] # 0번째 인덱스의 원소를 호출합니다.
print(result2)
print(heap)
# 20
# [20, 50]