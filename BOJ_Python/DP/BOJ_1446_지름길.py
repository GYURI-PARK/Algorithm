import sys

n, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dis = [i for i in range(d+1)]

for i in range(d+1):

    # 지름길로 간 거리와 고속도로로 간 거리를 비교
    dis[i] = min(dis[i], dis[i-1]+1)

    # 지름길을 반복하여 최단 거리를 찾는다.
    for start, end, short in graph:
        if i == start and end <= d and dis[i] + short < dis[end]:
            dis[end] = dis[i] + short

# 고속도로의 끝에 도착했을 때까지 걸린 거리를 출력
print(dis[d])

