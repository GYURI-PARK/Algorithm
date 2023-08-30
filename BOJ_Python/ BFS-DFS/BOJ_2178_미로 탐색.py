from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어날 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n-1][m-1]

    
print(bfs(0, 0))



# ===========================

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))

q = deque()

dx = [0,0,-1,1]
dy = [1,-1,0,0]

visited = [[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and visited[i][j] == 0:
      visited[i][j] = 1
      q.append((i,j))

      while q:
        tmp = q.popleft()

        for k in range(4):
          nx = tmp[0] + dx[k]
          ny = tmp[1] + dy[k]
        
          if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
          if graph[nx][ny] == 0:
            continue
        
          if graph[nx][ny] == 1:
            graph[nx][ny] = graph[tmp[0]][tmp[1]] + 1
            q.append((nx, ny))
  
print(graph[n-1][m-1])