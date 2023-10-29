from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

def bfs(start, end):
    q = deque()
    visited = [-1] * (100001)

    q.append(start)
    visited[start] = 0
    
    while q:
        x = q.popleft()

        if x == end:
            return visited[x]
        
        for i in (x-1, 2*x, x+1) :
            if 0 <= i <= 100000 and visited[i] == -1 and i == 2*x:
                q.appendleft(i)
                visited[i] = visited[x]
            elif 0 <= i <= 100000 and visited[i] == -1:
                q.append(i)
                visited[i] = visited[x] + 1

print(bfs(n, k))