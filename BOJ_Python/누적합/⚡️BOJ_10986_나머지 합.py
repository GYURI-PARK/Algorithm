import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

tmp = [0] * m
preSum = 0
for i in range(n):
    preSum += li[i]
    tmp[preSum % m] += 1

res = tmp[0] # 나머지가 0이 되는 경우의 수
for i in range(m):
    # 나머지가 0이 되는 경우의 수(3)의 조합 수
    # nC2 = n(n-1) / 2
    res += tmp[i] * (tmp[i] - 1) // 2
print(res)