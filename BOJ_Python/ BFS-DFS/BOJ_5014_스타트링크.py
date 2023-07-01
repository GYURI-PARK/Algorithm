from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs(start, goal):
    q = deque()
    visited = [-1] * (f + 1)

    q.append(start)
    visited[start] = 0

    while q:
        x = q.popleft()

        if x == goal:
            return visited[x]

        for i in (x + u, x - d):
            if 0 < i <= f and visited[i] == -1: # 층 수가 1부터 시작하므로 0이상의 조건을 붙일 필요가 없다.
                q.append(i)
                visited[i] = visited[x] + 1

    return "use the stairs"

print(bfs(s, g))