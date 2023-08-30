import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(t):
    m,n,k = map(int, sys.stdin.readline().split())
    graph = [[0] * n for _ in range(m)]
    q = deque()
    cnt = 0
   
    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    
    for k in range(m):
        for f in range(n):
            if graph[k][f] == 1:
                q.append((k,f))

                while q:
                    tmp = q.popleft()

                    for s in range(4):
                        nx = tmp[0] + dx[s]
                        ny = tmp[1] + dy[s]

                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        
                        if graph[nx][ny] == 1:
                            q.append((nx, ny))
                            # BFS 수행 후 1인 칸을 0으로 바꿔줌 -> BFS가 모두 끝나면 그 구역은 모두 0
                            graph[nx][ny] = 0
                # 1을 발견할 때마다 +1
                cnt += 1

    print(cnt)