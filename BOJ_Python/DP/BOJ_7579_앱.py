# https://claude-u.tistory.com/445

import sys

n, m = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
res = sum(cost)

dp = [[0 for _ in range(res+1)] for _ in range(n+1)]

for i in range(1, n+1):
    mem = memory[i-1]
    cos = cost[i-1]

    for j in range(1, res+1):
        if j < cos:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(mem + dp[i-1][j-cos], dp[i-1][j])

        if dp[i][j] >= m:
            res = min(res, j)
print(res)