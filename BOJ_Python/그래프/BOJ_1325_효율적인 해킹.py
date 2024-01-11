import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def bfs(node):
    q = deque([node])
    visited = [False] * (n+1)
    visited[node] = True
    cnt = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

res = []
max_cnt = 0

for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        res = []
        res.append(i)
    elif cnt == max_cnt:
        res.append(i)

print(*res)