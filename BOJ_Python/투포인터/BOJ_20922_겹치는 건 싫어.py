import sys

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

res = 0 
start, end = 0, 0

count = [0] * (max(num) + 1)

while end < n:
    if count[num[end]] < k:
        count[num[end]] += 1
        end += 1
    else:
        count[num[start]] -= 1
        start += 1
    res = max(res, end - start)

print(res)
    