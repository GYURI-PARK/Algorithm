import sys

def dfs(node, cnt):
    visited[node] = 1

    for n in graph[node]:
        # 모든 이웃 노드를 방문하고 cnt 반환
        if visited[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for j in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    
    print(dfs(1,0))