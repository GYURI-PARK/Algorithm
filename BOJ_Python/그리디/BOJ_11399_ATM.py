import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
ans = 0
tmp = 0
for i in range(n):
    tmp += li[i]
    ans += tmp

print(ans)