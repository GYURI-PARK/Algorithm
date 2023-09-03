import sys

m, n = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

start = 1
end = li[n-1]
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    
    # li의 각 원소들을 mid로 나눌 때 몫의 합이 m과 같을 때 mid 의 최댓값 
    for i in range(len(li)):
        cnt += li[i] // mid
    if cnt >= m:
        start = mid + 1
        res = max(mid, res)
    else:
        end = mid - 1

print(res)

# =================

import sys

m, n = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start = 1
end = int(1e9)
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    
    # li의 각 원소들을 mid로 나눌 때 몫의 합이 m과 같을 때 mid 의 최댓값 
    for i in range(len(li)):
        cnt += li[i] // mid
    if cnt >= m:
        start = mid + 1
        res = max(mid, res)
    else:
        end = mid - 1

print(res)