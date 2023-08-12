t = int(input())

# d[i] = i를 만드는데 나올 수 있는 경우의 수
# ex) D[4] = ?
# 1+1+1+1 , 3+1, 2+1+1, 1+2+1 => (3을 1,2,3의 합으로 나타내는 방법) + 1 = d[3]
# 1+1+2, 2+2 => (2를 1,2,3의 합으로 나타내는 방법) + 2 = d[2]
# 1+3 => (1을 1,2,3의 합으로 나타내는 방법) + 3 = d[1]
# d[4] = d[1] + d[2] + d[3]
# d[i] = d[i-1] + d[i-2] + d[i-3]

dp = [0 for _ in range(12)]
dp[0] = 0

for i in range(1, 12):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 2
    elif i == 3:
        dp[3] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(t):
    n = int(input())   
    print(dp[n])
