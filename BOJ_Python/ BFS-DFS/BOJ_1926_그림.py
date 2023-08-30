# BFS

from collections import deque
 
n, m = map(int, input().split())
graph = []
 
for i in range(n):
    graph.append(list(map(int, input().split())))
 
# 상하좌우 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1
 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count
 
paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))
 
 
if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))


# ==============================================================
# 2번

from collections import deque

n, m = map(int,input().split())
graph = []
max_area = 0
cnt = 0

q = deque()

for i in range(n):
  graph.append(list(map(int, input().split())))

# 상하좌우 중에 하나도 1인게 없으면(= BFS의 시작점이 될 수 있는 곳) cnt += 1
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 방문 확인 배열
visited = [[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):

    # 그림이 있고 방문한 적이 없는 경우
    if graph[i][j] == 1 and visited[i][j] == 0:
      visited[i][j] = 1
      cnt += 1
      area = 1 # 현재 탐색 중인 그림의 크기
      q.append((i, j))

      while q:
        tmp = q.popleft()

        for k in range(4):
          nx = tmp[0] + dx[k]
          ny = tmp[1] + dy[k]

          # 범위 이탈 시
          if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
          # 이미 방문 했거나, 그림이 없다면
          if visited[nx][ny] == 1 or graph[nx][ny] == 0:
            continue
          
          visited[nx][ny] = 1
          area += 1
          q.append((nx, ny))
      
      if max_area < area:
        max_area = area

print(cnt)
print(max_area)