# 시간 초과

# n = int(input())

# def dp(n):
#     res = 0
#     if n == 0:
#         res = 1

#     else:
#         for i in range(n):
#             res += dp(i) * dp(n-i-1)

#     return res

# print(dp(n))

# ==================

dp = [0] * 36
dp[0] = 1

n = int(input())
res = 0

for i in range(1, n+1):
    dp[i] = dp[i-1] * dp[i-1]
    res += dp[i]

print(res)