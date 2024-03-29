import sys

num = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(num+1)]
# dp[n][k] : n자리 수, k는 끝 숫자

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, num+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[num]) % 1000000000)