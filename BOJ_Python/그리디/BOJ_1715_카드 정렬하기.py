import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

res = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    res += a
    res += b
    heapq.heappush(heap, a+b)

print(res)


# print(heap)