import sys

n, m = map(int, sys.stdin.readline().split())
dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    day, pages = map(int, sys.stdin.readline().split())

    for j in range(1, n+1):
        if (j - day) >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day] + pages)
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[m][n])