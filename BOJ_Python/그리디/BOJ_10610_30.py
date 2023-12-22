import sys

n = list(map(int, sys.stdin.readline().rstrip()))
tmp = 0
n.sort(reverse=True)
res = ''
for i in range(len(n)):
    tmp += n[i]
    res += str(n[i])

if tmp % 3 != 0 or 0 not in n:
    print(-1)
else:
    print(res)
