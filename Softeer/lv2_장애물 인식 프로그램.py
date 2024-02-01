import sys
from collections import deque

n = int(sys.stdin.readline())
map = [sys.stdin.readline().rstrip() for _ in range(n)]

visited = [[False] * (n) for _ in range(n)]

res = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = int(x) + dx[i]
            ny = int(y) + dy[i]

            if -1 < nx < n and -1 < ny < n:
                if not visited[nx][ny] and map[nx][ny] == '1':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    res.append(cnt)
            



for i in range(n):
    for j in range(n):
        if map[i][j] == '1' and not visited[i][j]:
            bfs(i,j)

print(len(res))
res.sort()
print(*res, sep='\n')