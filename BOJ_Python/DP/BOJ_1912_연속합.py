import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

dp = [0] * n
dp[0] = li[0]

for i in range(1, n):
    dp[i] = max(li[i], dp[i-1]+li[i])

print(max(dp))