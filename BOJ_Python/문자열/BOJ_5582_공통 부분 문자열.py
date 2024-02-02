import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

res = 0
dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]

for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        if t[j-1] == s[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            res = max(res, dp[i][j])

print(res)