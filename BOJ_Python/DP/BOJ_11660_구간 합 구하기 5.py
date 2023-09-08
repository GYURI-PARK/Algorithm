# 시간초과

import sys

# n, m = map(int, sys.stdin.readline().split())
# graph = []

# def get_sum(li):
#     sum_tmp = 0 
#     for j in range(li[0], li[2]+1):
#         for k in range(li[1], li[3]+1):
#             sum_tmp += graph[j-1][k-1]
#     return sum_tmp

# for i in range(n):
#     tmp = list(map(int, sys.stdin.readline().split()))
#     graph.append(tmp)

# for i in range(m):
#     test = list(map(int, sys.stdin.readline().split()))
#     result = get_sum(test)
#     print(result)

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + graph[i-1][j-1]

# for i in range(m):
#     test = list(map(int, sys.stdin.readline().split()))
#     result = dp[test[2]][test[3]] - dp[test[2]][test[1]-1] - dp[test[0]-1][test[3]] + dp[test[0]-1][test[1]-1]
#     print(result)

print(dp)