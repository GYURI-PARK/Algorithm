# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

import sys

n = int(sys.stdin.readline())
dp = []
for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

# dp[i][j] = i행 j열까지의 최대합
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]

print(max(dp[n-1]))
print(dp)