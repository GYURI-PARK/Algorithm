import sys
sys.setrecursionlimit(10**6)

# 재귀 dfs
n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
parent = [0] * (n+1)

def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)

for i in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, n+1):
    print(parent[i])