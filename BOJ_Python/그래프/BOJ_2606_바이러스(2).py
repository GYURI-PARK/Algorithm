import sys
from collections import deque

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def bfs(node):
    global cnt
    q = deque(graph[node])
    visited[node] = True
    
    while q:
        a = q.pop()
        if not visited[a]:
            bfs(a)
            cnt += 1
bfs(1)
print(cnt)