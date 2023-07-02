from collections import deque

m, n = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)

# =============================================

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 익은 토마토(1)의 좌표를 큐에 저장
            q.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):

        # 익은 토마토 상하좌우 돌면서 일수 저장
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

ans = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            # 안익은 토마토(0)이 있으면 바로 정지
            print(-1)
            exit()
    ans = max(ans, max(line))

# 1에서 시작했기 때문에 결과 값에서 1빼주기
print(ans-1)