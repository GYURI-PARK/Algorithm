# import sys

# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())

# def palindrome(start, end):
#     if li[start-1:end] == li[start-1:end][::-1]:
#         return 1
#     else:
#         return 0
        
# for i in range(m):
#     start, end = map(int, sys.stdin.readline().split())
#     print(palindrome(start, end))



# dp 사용해서 풀어야됨

import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if li[i] == li[i+1]:
        dp[i][i+1] = 1
    else:   
        dp[i][i+1] = 0
for i in range(n-2):
    for j in range(n-2-i):
        tmp = i + j + 2
        if li[j] == li[tmp] and dp[j+1][tmp-1] == 1:
            dp[j][tmp] = 1
        else:
            dp[j][tmp] = 0 

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[start-1][end-1])