# import sys

# t = int(sys.stdin.readline())
# dp = [1, 1]

# for i in range(t):
#     p, q = map(int, sys.stdin.readline().split())
#     if p == 1 or p ==2:
#         print(1)
#     else:
#         for j in range(2, p+1):
#             dp.append(dp[j-1] + dp[j-2])
#         print("Case #", i+1, ": ", dp[p-1] % q, sep='')

# 시간초과

import sys

dp = [1,1]
for i in range(2, 10001):
    dp.append(dp[i-1]+ dp[i-2])

t = int(sys.stdin.readline())
for i in range(t):
    p, q = map(int, sys.stdin.readline().split())
    if p == 0 or p == 1:
        print("Case #", i+1, ": ", 1 % q, sep='')
    else:
        print("Case #", i+1, ": ", dp[p-1] % q, sep='')