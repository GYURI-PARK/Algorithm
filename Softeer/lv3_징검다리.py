import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    tmp = 0
    for j in range(i):
        if li[i] > li[j]:
            if tmp < dp[j]:
                tmp = dp[j]
    dp[i] = tmp + 1

print(max(dp))
