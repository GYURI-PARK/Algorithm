import sys

n = int(sys.stdin.readline())

# dp

if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3:
    print(3)
else:
    dp = [0,1,2,3]
    for i in range(4, n+1):
        min_val = 1e9
        j = 1
        while (j*j) <= i:
            min_val = min(min_val, dp[i - (j*j)])
            j += 1
        dp.append(min_val + 1)
    print(dp[n])