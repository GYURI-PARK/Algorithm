import sys

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
diff = []

for i in range(0, n-1):
    diff.append(li[i+1]-li[i])

diff.sort()
ans = 0

for i in range(n-k):
    ans += diff[i]

print(ans)
