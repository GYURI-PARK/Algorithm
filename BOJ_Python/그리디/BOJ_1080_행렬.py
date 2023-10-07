import sys

n, m = map(int, sys.stdin.readline().split())
prev = []
for i in range(n):
    prev.append(list(map(int, sys.stdin.readline().rstrip())))
next = []
for i in range(n):
    next.append(list(map(int, sys.stdin.readline().rstrip())))

def change(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if prev[x][y] == 0:
                prev[x][y] = 1
            else:
                prev[x][y] = 0
    
res = 0

if (n < 3 or m < 3) and prev != next:
    res = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if prev[i][j] != next[i][j]:
                res += 1
                change(i,j)

if res != -1:
    if prev != next:
        res = -1
        
print(res)
