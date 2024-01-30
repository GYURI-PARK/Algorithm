import sys

n, k = map(int, sys.stdin.readline().split())
stuff = [[0, 0]]

backpack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    stuff.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            backpack[i][j] = backpack[i-1][j]
        else:
            backpack[i][j] = max(value + backpack[i-1][j-weight], backpack[i-1][j])

print(backpack)

