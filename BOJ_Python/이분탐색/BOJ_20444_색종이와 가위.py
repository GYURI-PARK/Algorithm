import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0], [2] , [3,4]] + [[0] for _ in range(n-2)]

if n > 2:
    dp[1] = [2]
    dp[2] = [3,4]

    for i in range(3, n+1):
        dp[i] = list(set([dp[i-1][0] + 1, dp[i-1][0] * 2, (dp[i-1][-1] // 2) + ((dp[i-1][-1] // 2) * 2)]))
        dp[i].sort()

start, end = 0 , len(dp[n])-1

while start <= end:
    mid = (start + end) // 2 

    if k < dp[n][mid]:
        end = mid - 1
    else:
        start = mid + 1
    
    # 아래처럼 쓸땐 dp[n][start] 값과 비교 
    # if k > dp[n][mid]:
    #     start = mid + 1
    # else:
    #     end = mid - 1 

if end >= 0 and dp[n][end] == k:
    print("YES")
else:
    print("NO")


# =======================
    
n, k = map(int, sys.stdin.readline().split())
start, end = 0, n // 2
# isPossible = False

# while start <= end:
#     rowCut = (start + end) // 2
#     colCut = n - rowCut
#     cnt = (rowCut + 1) * (colCut + 1)

#     if k == cnt:
#         print("YES")
#         isPossible = True
#         break
#     if k > cnt:
#         start = cnt + 1
#     else:
#         end = cnt - 1

# if not isPossible:
#     print("NO")

cnt = 0
while start <= end:
    mid = (start + end) // 2
    cnt = (mid + 1) * (n - mid + 1) # (가로컷 + 1) * (세로컷 + 1)

    if cnt < k:
        start = mid + 1
    elif cnt > k:
        end = mid - 1
    else:
        break
if cnt == k:
    print("YES")
else:
    print("NO")
