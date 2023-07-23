import sys

n, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dis = [i for i in range(d+1)]

for i in range(d+1):

    # 지름길로 간 거리와 고속도로로 간 거리를 비교
    # 한칸 전 위치의 테이블 값 + 1이 현재 테이블 값보다 작다면 현재 테이블 값을 한칸전 위치의 테이블 + 1로 바꾼다.
    dis[i] = min(dis[i], dis[i-1]+1)

    # 지름길을 반복하여 최단 거리를 찾는다.
    for start, end, short in graph:
        if i == start and end <= d and dis[i] + short < dis[end]:
            # 현재 위치에 지름길이 있다면 (지름길로 건너간 곳의 원래 테이블 값)과 (지름길로 건너가기 전의 테이블 값+지름길의 거리) 중 더 작은 값으로 건너간 곳의 값을 바꾼다. 
            dis[end] = dis[i] + short

# 고속도로의 끝에 도착했을 때까지 걸린 거리를 출력
print(dis[d])

