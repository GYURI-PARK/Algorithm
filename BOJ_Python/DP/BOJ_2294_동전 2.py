import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]

dp = [float('inf') for _ in range(k+1)]
dp[0] = 0

for i in range(1, k+1):
    for j in coin:
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])