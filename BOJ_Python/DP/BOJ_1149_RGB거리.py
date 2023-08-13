# 1. 테이블 정의하기
# dp[i][0] = i번째 집까지 칠할 때 비용의 최솟값, 단 i번째 집은 빨강
# dp[i][1] = i번째 집까지 칠할 때 비용의 최솟값, 단 i번째 집은 초록
# dp[i][2] = i번째 집까지 칠할 때 비용의 최솟값, 단 i번째 집은 파랑

# 2. 점화식 찾기
# i번째가 빨강일 경우, i-1번쨰는 초록 혹은 파랑이어야 한다.
# dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + red[k](cost[k][0])
# dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + green[k](cost[k][1])
# dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + blue[k](cost[k][2])

# 3. 초기값 정하기
# dp[1][0] = red[1] = cost[0][0]
# dp[1][1] = green[1] = cost[1][1]
# dp[1][2] = blue[1] = cost[2][2]

import sys

n = int(sys.stdin.readline())
dp = []

for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[n-1]))