import sys

n = int(sys.stdin.readline())
llist = [0] + list(map(int, sys.stdin.readline().split()))
hlist = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
    l, h = llist[i], hlist[i]
    for j in range(1, 101):
        if j < l:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-l] + h)
    
print(dp)


# 배낭정리의 기본 개념은,

# 1. i 번째 물건을 배낭에 넣을 수 없다.
#    -> i-1 개의 물건들을 갖고 구한 전 단계의 값을 그대로 가져온다.
# 2. i 번째 물건을 배낭에 넣을 수 있다.
#    -> max(i-1 개의 물건들을 갖고 구한 전 단계의 값, i 번째 물건만큼의 무게를 비웠을 때의 값 + i 번째 물건)
