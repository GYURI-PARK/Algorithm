import sys

n, jm, hs = map(int, sys.stdin.readline().split())

res = 0

while jm != hs:

    jm -= jm // 2
    hs -= hs // 2
    res += 1

print(res)