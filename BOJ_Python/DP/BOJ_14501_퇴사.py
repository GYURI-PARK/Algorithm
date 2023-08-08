# Bottom-up

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

# dp[i] = i번째 날까지 일을 했을 때 얻을 수 있는 최대 보상
dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+schedule[i][0], n+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
    print(dp)
print(dp[-1])

# =============================================

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + schedule[i][0] > n:
        dp[i] = dp[i+1]

    else:
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i + schedule[i][0]])

print(dp[0])