# 1. 테이블 정의하기
# dp[i] = 2*i 크기의 직사각형을 채우는 방법의 수

# 2. 점화식 찾기
# dp[i] = dp[i-1] + dp[i-2]
# <img width="1278" alt="image" src="https://github.com/GYURI-PARK/Indieplus_Pohang/assets/93391058/2be1b506-81d0-4f30-bddd-d1e02bea4762">

# 3. 초기값 정하기
# dp[1] = 1
# dp[2] = 2

import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2 
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
