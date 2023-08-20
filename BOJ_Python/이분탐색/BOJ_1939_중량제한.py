import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
li = [[] for _ in range(n+1)] 

for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    li[a].append([b,c])
    li[b].append([a,c])

one, two = map(int, sys.stdin.readline().split())

start = 1
end = 1000000000
res = 0

def bfs(weight):
    queue = deque()
    queue.append(one)
    visited = [False] * (n+1)
    visited[one] = True

    while queue:
        x = queue.popleft()

        for i, w in li[x]:
            if not visited[i] and w >= weight:
                visited[i] = True
                queue.append(i)

    if visited[two]:
        return True
    else:
        return False

while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)