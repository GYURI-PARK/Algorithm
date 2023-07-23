import sys
import heapq

n,m,x = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append((end, time))

def dijkstra(start):
    pq = []
    distance = [INF] * (n+1)

    distance[start] = 0
    heapq.heappush(pq, (distance[start], start))

    while pq:
        dist, now = heapq.heappop(pq)
        # 기존 최단거리보다 멀 경우, 무시
        if distance[now] < dist:
            continue

        # 인접노드 탐색
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            # 기존 거리보다 짧을 경우
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(pq, (cost, node_index))      
    return distance

res = 0
for i in range(1, n+1):
    # 각 마을을 출발지점으로 했을 때의 최단 거리를 나타내는 리스트
    go = dijkstra(i) 
    
    # 출발지점 x를 기준으로 각 마을까지의 최단 거리를 나타내는 리스트
    back = dijkstra(x) 
    
     # 모든 마을을 출발지점으로 했을 때와 출발지점 x를 기준으로 각 마을까지의 거리의 합을 구하여 그 중 가장 큰 값을 res에 저장
    res = max(res, go[x] + back[i])

print(res)