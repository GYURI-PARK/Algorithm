# dp[i][j] = 첫번쨰 문자열에서 i번쨰, 두번째 문자열에서 j번째까지의 공통된 문자들
import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

dp = [[""] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + s1[i-1]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(dp)
print(dp[len(s1)][len(s2)])