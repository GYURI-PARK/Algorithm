import sys

# dp 
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
INF = 999999999
dp = [0] + [INF] * (n-1)

# dp[i] = i번째 돌까지 가는데 드는 최소의 힘

for i in range(1, n):
    for j in range(0, i):
        power = max((i-j) * (1+abs(li[i]-li[j])), dp[j])
        dp[i] = min(dp[i], power)
print(dp[n-1])