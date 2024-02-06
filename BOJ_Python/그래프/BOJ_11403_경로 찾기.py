import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
G = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
graph = [[] * (n+1) for _ in range(n+1)]
visited = [[False] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if G[i][j] == 1:
            graph[i+1].append(j+1)

def bfs(node):
    q = deque(graph[node])

    while q:
        new = q.pop()
        if not visited[new]:
            visited[new] = True
            bfs(new)
            
            
for i in range(1, n+1):
    bfs(i)
    
print(graph)