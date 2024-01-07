import sys

n, m = map(int, sys.stdin.readline().split())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

start, end = 0, 0
res = 2000000000
while end < n and start < n:
    if num[end] - num[start] < m:
        end += 1
    else:
        res = min(res, num[end]-num[start])
        start += 1

print(res)