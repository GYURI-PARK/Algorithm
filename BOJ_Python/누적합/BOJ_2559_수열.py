import sys

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

res = []
res.append(sum(li[:k]))

for i in range(n-k):
    res.append(res[i] - li[i] + li[k+i])

print(max(res))