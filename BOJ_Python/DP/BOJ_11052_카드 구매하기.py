import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

dp = card[:]
for i in range(n):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j-1] + card[j])

print(dp[n-1])