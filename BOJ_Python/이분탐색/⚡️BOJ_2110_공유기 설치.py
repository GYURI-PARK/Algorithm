import sys

n, c = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()

start, end = 1, li[-1] - li[0] # 공유기 사이의 거리를 이진탐색
res = 0

while start <= end:
    mid = (start + end) // 2 # 현재 공유기 사이의 거리
    tmp = li[0]
    cnt = 1

    for i in range(1, n):
        if li[i] >= tmp + mid:
            cnt += 1
            tmp = li[i]
    
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)