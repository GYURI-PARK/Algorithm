# import sys

# a = sys.stdin.readline().rstrip()
# b = sys.stdin.readline().rstrip()
# c = sys.stdin.readline().rstrip()

# tmp = ''

# for i in range(1, len(a)+1):
#     for j in range(1, len(b)+1):
#         if a[i-1] == b[j-1]:
#             tmp += a[i-1]

# dp = [[0] * (len(c) + 1) for _ in range(len(tmp) + 1)]

# for i in range(1, len(tmp)+1):
#     for j in range(1, len(c)+1):
#         if tmp[i-1] == c[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# print(dp[-1][-1])

import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
c = sys.stdin.readline().rstrip()

dp = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):
            if a[i-1] == b[j-1] == c[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])


print(dp[-1][-1][-1])

