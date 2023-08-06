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

n = int(input())
dp = [1, 1, 2]

for i in range(3, n+1):
    tmp = 0
    for j in range(i):
        tmp += dp[j] * dp[i-j-1]
    dp.append(tmp)

print(dp[n])