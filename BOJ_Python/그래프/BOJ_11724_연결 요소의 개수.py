import sys
sys.setrecursionlimit(5000)
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
res = 0

for i in range(1, n+1):
    if not visited[i]:
        res += 1
        dfs(i)

# print(res)

# def bfs(node):
#     q = deque()
#     q.append(node)
#     visited[node] = True

#     while q:
#         x = q.popleft()
#         for i in graph[x]:
#             if not visited[i]:
#                 visited[i] = True
#                 q.append(i)

