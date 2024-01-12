# dfs 풀이
import sys

n, m = map(int, sys.stdin.readline().split())
li = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    li[a].append(b)
    li[b].append(a)

visited = [False] * (n+1)
cnt = 0
res = []
def dfs():
    global cnt
    if len(res) == 3:
        cnt += 1
        return
    for i in range(1, n+1):
        tmp = 0
        if len(res) > 0 and i <= res[-1]:
            continue
        for j in res:
            if li[i-1][j] > 0:
                tmp = 1
                break
        if tmp == 1:
            continue
        res.append(i)
        dfs()
        res.pop()

dfs()
print(cnt)   


# for문 풀이
import sys

n, m = map(int, sys.stdin.readline().split())
icecream = [[False for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    icecream[a-1][b-1] = True
    icecream[b-1][a-1] = True

res = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not icecream[i][j] and not icecream[i][k] and not icecream[j][k]:
                res += 1

print(res)