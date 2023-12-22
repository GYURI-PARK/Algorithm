import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

ans = 0

a.sort()
b.sort(reverse=True)

for i in range(n):
    ans += a[i] * b[i]

print(ans)