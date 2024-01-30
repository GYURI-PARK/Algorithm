import sys

n, k = map(int, sys.stdin.readline().split())
stuff = [[0,0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

bp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        val = stuff[i][1]

        if j < weight:
            bp[i][j] = bp[i-1][j]
        else:
            bp[i][j] = max(bp[i-1][j], val + bp[i-1][j-weight])
print(bp[n][k])