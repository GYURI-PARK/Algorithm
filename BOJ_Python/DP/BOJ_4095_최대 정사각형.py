# import sys

# while True:
#     row, col = list(map(int, sys.stdin.readline().split()))
#     res = 0
#     if row == 0 and col == 0:
#         break
#     else:
#         dp = []
#         for i in range(row):
#             dp.append(list(map(int, sys.stdin.readline().split())))
    
#     for i in range(row):
#         for j in range(col):
#             if dp[i][j] == 0:
#                 continue
#             else:
#                 for k in range(row-i):
#                     if dp[i+1][j] == 1 and dp[i][j+1] == 1:
import sys

while True:
    row, col = map(int, sys.stdin.readline().split())
    if row == 0 and col == 0:
        break

    square = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
    dp = [[0] * (col+1) for _ in range(row+1)]
    # (i, j) 위치를 우측 하단 모서리로 갖는 최대 정사각형의 한 변의 길이

    max_length = 0

    for i in range(1, row+1):
        for j in range(1, col+1):
            if square[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
    print(max_length)