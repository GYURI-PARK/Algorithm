import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# # 양수인 것만 다 더하면 됨
# tmp = 0
# res = 0
# for i in range(0, n):
#     for j in range(0, m):
#         if graph[i][j] > 0: 
#             tmp += graph[i][j]
#         else:
#             if res < tmp:
#                 res = tmp
#                 print('res' , res)
#             break

#         for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]

#                 if nx > 0 and nx < n and ny > 0 and ny < m:
#                     if graph[nx][ny] > 0:
#                         tmp += graph[nx][ny]        

# print(res)

tmp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        tmp[i][j] = graph[i-1][j-1] + tmp[i][j-1] + tmp[i-1][j] - tmp[i-1][j-1]

res = int(-10e9)

for x1 in range(1, n+1):
    for y1 in range(1, m+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1, m+1):
                res = max(res, tmp[x2][y2] - tmp[x1-1][y2] - tmp[x2][y1-1] + tmp[x1 - 1][y1 - 1])
print(res)


# ================================================================================

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]

res = int(-10e9)

for i in range(1, n+1):
    row = [0] * (m+1)

    # i행부터 각 열끼리의 누적합
    for j in range(i, n+1):
        col = [0] * m
        for k in range(1, m+1):

            # i행 ~ j행까지 k열의 누적합
            row[k] += graph[j-1][k-1]
            col[k-1] = max(col[k-2] + row[k], row[k])
        tmp = max(col)
        if tmp > res:
            res = tmp

print(res)