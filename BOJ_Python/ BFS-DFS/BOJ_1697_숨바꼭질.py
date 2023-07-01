from collections import deque

n, k = map(int, input().split())

def bfs(start, end):
    q = deque()
    visited = [0] * (100001)

    q.append(start)
    while q:
        x = q.popleft()

        if x == end:
            return visited[x]
        
        for i in (x-1, x+1, 2*x) :
            if 0 <= i <= 100000 and not visited[i]:
                q.append(i)
                visited[i] = visited[x] + 1


print(bfs(n, k))