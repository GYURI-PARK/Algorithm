import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)


for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 리프노드일 때 = 단절점 아님
def vertex(node):
    if len(graph[node]) == 1:
        return "no"
    else:
        return "yes"

# 트리는 사이클이 존재하지 않으므로 모든 간선이 단절선이다. 따라서 항상 yes를 출력
q = int(sys.stdin.readline())
for i in range(q):
    t, k = map(int, sys.stdin.readline().split())
    tmp = 0
    if t == 1:
        print(vertex(k))
    else:
        print("yes")