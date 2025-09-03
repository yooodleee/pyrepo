import heapq


heap_items = [1, 3, 5, 7, 9]

max_heap = []
for item in heap_items:
	heapq.heappush(max_heap, (-item, item))
print(max_heap)
# [(-9, 9), (-7, 7), (-3, 3), (-1, 1), (-5, 5)]

max_item = heapq.heappop(max_heap)[1]
print(max_item)
# 9