import sys
from collections import deque

n = int(sys.stdin.readline())
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
li = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    li[x].append(y)
    li[y].append(x)

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        new = q.popleft()
        for n in li[new]:
            if visited[n] == 0:
                visited[n] = visited[new] + 1
                q.append(n)
        
bfs(a)

if visited[b] < 1:
    print(-1)
else:
    print(visited[b])