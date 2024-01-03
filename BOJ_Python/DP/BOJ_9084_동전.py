import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    dp = [0] * (m+1)
    dp[0] = 1

    for j in coin:
        for k in range(m+1):
            if k >= j:
                dp[k] += dp[k - j]
            
    print(dp[m])