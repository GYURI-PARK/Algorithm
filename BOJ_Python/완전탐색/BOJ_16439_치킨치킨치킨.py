import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
chicken = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

maxSum = 0

for a, b, c in combinations(range(m), 3):
    tmp = 0
    for i in range(n):
        tmp += max(chicken[i][a], chicken[i][b], chicken[i][c])
    maxSum = max(tmp, maxSum)

print(maxSum)