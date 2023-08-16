import sys

t = int(sys.stdin.readline())
k = int(sys.stdin.readline())

coin = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

dp = [0] * (t+1)
dp[0] = 1

for p, n in coin:
    for i in range(t, 0 ,-1):
        for j in range(1, n+1):
            ans = i - (p*j)
            if ans >= 0:
                dp[i] += dp[ans]
        print(dp)

print(dp[t])
