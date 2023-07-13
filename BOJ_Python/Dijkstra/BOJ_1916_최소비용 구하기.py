import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 입력값을 담을 리스트
graph = [[] for _ in range(n+1)]
# 방문 처리 기록
# visited = [False] * (n + 1)


for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

start, end = map(int, sys.stdin.readline().split())


def dijkstra(graph, start):
    # 거리용
    distance = [int(1e9)] * (n+1)
    # 1부터 차례대로 거리 확인 -> 가장 작은 값을 가진 노드부터 다시 인접 노드 탐색
    pq = []
    distance[start] = 0
    heapq.heappush(pq, [distance[start], start])
    

    while pq:
        dist, node = heapq.heappop(pq)

        # 기존 최단거리보다 멀 경우, 무시
        if distance[node] < dist:
            continue

        # 인접노드 탐색
        for next_node, next_dist in graph[node]:
            nd = dist + next_dist

            # 기존 거리보다 짧을 경우
            if nd < distance[next_node]:
                distance[next_node] = nd
                heapq.heappush(pq,[nd, next_node])

    return distance

res = dijkstra(graph, start)

print(res[end])