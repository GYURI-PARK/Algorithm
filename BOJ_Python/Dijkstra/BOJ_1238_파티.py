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
        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(pq, (cost, node_index))

    return distance

res = 0
for i in range(1, n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    res = max(res, go[x] + back[i])

print(res)