import sys

c, n = map(int, sys.stdin.readline().split())
# dp = [[1000] * (c+1) for _ in range(n+1)]
dp = [1e7 for _ in range(c + 100)]
dp[0] = 0
li = []

for i in range(1, n+1):
    li.append(list(map(int, sys.stdin.readline().split())))

for cost, people in li:
    for i in range(people, c+100):
        dp[i] = min(dp[i-people]+cost, dp[i])

print(min(dp[c:]))