import sys

n, k = map(int, sys.stdin.readline().split())
coin = []

for i in range(n):
    coin.append(int(sys.stdin.readline()))

ans = 0

for i in reversed(range(n)):
    ans += k // coin[i]
    k = k % coin[i]

print(ans)