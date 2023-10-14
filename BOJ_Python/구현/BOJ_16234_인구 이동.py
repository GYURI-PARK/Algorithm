import sys
from collections import deque

n,l,r = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i,j):
    queue = deque()
    union = []
    queue.append((i,j))
    union.append((i,j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not visited and 0 <= nx < n and 0 <= ny < n:
                if l <= abs(graph[nx][ny] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union


print(bfs(0,0))
