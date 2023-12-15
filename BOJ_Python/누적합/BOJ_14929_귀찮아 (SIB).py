import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

prefix = 0
ans = 0

for i in range(n-1):
    prefix += li[i]
    ans += li[i+1] * prefix

print(ans)

# x1x2 + x1x3 + x1x4 + x2x3 + x2x4 + x3x4
# x1(x2 + x3 + x4) + x2(x3 + x4) + x3(x4)
# x1x2 + (x1 + x2)x3 + (x1 + x2 + x3)x4