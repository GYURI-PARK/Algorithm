import sys

n = int(sys.stdin.readline())

for i in range(n):
    t = int(sys.stdin.readline())
    dp = [[0, 0]] * (t+1)

    if t > 1:
        dp[0] = [1, 0]
        dp[1] = [0, 1]
        for j in range(2, t+1):
            dp[j] = dp[j-1][0] + dp[j-2][0], dp[j-1][1] + dp[j-2][1]
        print(dp[t][0], dp[t][1])
    elif t == 0:
        print(1, 0)
    elif t == 1:
        print(0, 1)