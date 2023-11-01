import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(v+1)]

for i in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    tree[a].append([w,b])
    tree[b].append([w,a])

visited = [False] * (v+1)

# 최소 힙
# 가중치 순으로 정렬 -> 최소 cost 선택
q = [[0,1]]

ans = 0 # 가중치 합
cnt = 0 # 간선의 수

while q:
    # 간선은 최대 v-1개
    if cnt == v:
        break
    w, s = heapq.heappop(q)
    if not visited[s]:
        visited[s] = True
        ans += w
        cnt += 1
        for i in tree[s]:
            heapq.heappush(q, i)
print(ans)