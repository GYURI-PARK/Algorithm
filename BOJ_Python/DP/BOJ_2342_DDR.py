# ❌❌❌ 아진짜 못풀겠음 ❌❌❌

import sys
# 재귀의 최대 깊이를 10 ** 6으로 설정 (원래 파이썬 최대 깊이 1000)
sys.setrecursionlimit(10 ** 6)

li = list(map(int, sys.stdin.readline().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]

def score(a,b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(a-b) % 2 == 0:
        return 4
    else:
        return 3
    
# ddr(n,l,r) : 발의 위치가 (l, r)일 때, n번째 발판부터 밟았을 때 소모되는 힘
def ddr(n, l, r):
    global dp

    if n >= len(li) - 1:
        return 0
    
    if dp[n][l][r] != -1:
        return dp[n][l][r]
    
    # 왼쪽 발이 움직일 경우 or 오른쪽 발이 움직일 경우
    dp[n][l][r] = min(ddr(n + 1, li[n], r) + score(l, li[n]), 
                      ddr(n + 1, l, li[n]) + score(r, li[n]))
    
    return dp[n][l][r]


print(ddr(0,0,0))