import sys

n = int(sys.stdin.readline())
lope = []
res = []

for i in range(n):
    lope.append(int(sys.stdin.readline()))

lope.sort()
for i in range(n):
    res.append(lope[i] * (n-i))

print(max(res))