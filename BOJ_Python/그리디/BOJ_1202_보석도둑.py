# ❗️ 용량이 작은 가방부터 채워야됨 ❗️
# 보석용량 < 최대 용량 and 최대가격

import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
rubik = []
for i in range(n):
    heapq.heappush(rubik,list(map(int, sys.stdin.readline().split())))

bag = []
for i in range(k):
    bag.append(int(sys.stdin.readline()))

rubik.sort()
bag.sort()

res = 0
tmp = [] # 가방안에 들어갈 수 있는 모든 보석들


for i in bag:
    while rubik and rubik[0][0] <= i:
        heapq.heappush(tmp, -rubik[0][1])
        heapq.heappop(rubik)

    if tmp:
        res -= heapq.heappop(tmp)

print(res)