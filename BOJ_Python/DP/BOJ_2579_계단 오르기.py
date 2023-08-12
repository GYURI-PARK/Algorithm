# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

# 총 점수의 최댓값을 구하는 프로그램

# 1. 테이블 정의하기 
# dp[i][j] = 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 때 점수 합의 최댓값, 
# 단 i번째 계단은 반드시 밟아야 함
# * 지금까지 몇개의 계단을 밟았는지에 대한 정보가 필요하기 때문 !

# 2. 점화식 찾기
# dp[k][1] -> 지금까지 1개의 계단을 연속해서 밟고 k번째 계단까지 올라섰을 때의 최댓값이므로 k-1번째의 계단을 밟지 않았다는 의미
# 따라서 k-2번째 계단을 밟앗다는 것은 자먕
# dp[k][1] = max(dp[k-2][1], dp[k-2][2]) + stair[k]
# dp[k][2] = dp[k-1][1] + stair[k]

# 3. 초기값 정하기
# dp[1][1] = stair[1], dp[1][2] = 0
# dp[2][1] = stair[2], dp[2][2] = stair[1] + stair[2]

import sys

n = int(sys.stdin.readline())
dp = [[0] * 2 for _ in range(n)]
stair = [ int(sys.stdin.readline()) for _ in range(n)]

if n == 1 or n == 2:
    print(sum(stair))
else:   
    dp[0][0] = stair[0]
    dp[0][1] = 0
    dp[1][0] = stair[1]
    dp[1][1] = stair[0] + stair[1]
    for i in range(2, n):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stair[i]
        dp[i][1] = dp[i-1][0] + stair[i]

    print(max(dp[-1]))

# ============
# 1차원 dp

n = int(input()) 
s = [int(input()) for _ in range(n)] 
dp = [0]*(n) 
if len(s) <= 2: 
    print(sum(s))
else: 
    dp[0] = s[0] 
    dp[1] = s[0]+s[1] 
    for i in range(2, n):
        dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])