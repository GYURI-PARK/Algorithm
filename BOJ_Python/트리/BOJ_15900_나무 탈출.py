import sys
sys.setrecursionlimit(600000)

# 각각의 노드의 깊이를 구해주는 함수
def dfs(node):
    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            depth[i] = depth[node] + 1
            dfs(i)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
ans = 0

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for i in range(2, n+1):
    # 리프노드일 때
    if len(graph[i]) == 1:
        ans += depth[i]

if (ans % 2) == 0:
    print("No")
else:
    print("Yes")