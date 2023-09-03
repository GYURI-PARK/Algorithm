import heapq

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 1

def dijkstra():
    pq = []
    heapq.heappush(pq, (graph[0][0], 0 , 0))
    distance[0][0] = 0

    while pq:
        cost, x, y = heapq.heappop(pq)
        # 마지막 좌표
        if x == n-1 and y == n-1:
            print(f'Problem {cnt}: {distance[x][y]}')
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))


while True:
    n = int(input())
    if n == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[int(1e9)] * n for _ in range(n)]
    dijkstra()
    cnt += 1