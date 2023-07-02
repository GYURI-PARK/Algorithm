from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs(start, goal):
    q = deque()
    visited = [-1] * (f + 1)

    q.append(start)
    visited[start] = 0     # 방문한 정점 확인

    while q:
        x = q.popleft()

        if x == goal:
            return visited[x]

        for i in (x + u, x - d):
            if 0 < i <= f and visited[i] == -1: # 층 수가 1부터 시작하므로 0 이상의 조건을 붙일 필요가 없다.
                q.append(i)
                visited[i] = visited[x] + 1

    return "use the stairs"

print(bfs(s, g))


# ---------------------------------------------------------------------------------------------------


from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs(start, goal):
    q = deque()
    visited = [0] * (f + 1)

    q.append(start)
    visited[start] = 1

    while q:
        x = q.popleft()

        if x == goal:
            return visited[x] - 1

        for i in (x - d, x + u):
            if 1 <= i <= f and visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1

    return "use the stairs"

print(bfs(s, g))

# ---------------------------------------------------------------------------------------------------

from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs(start, goal):
    q = deque()
    visited = [0] * (f + 1)

    q.append(start)
    visited[start] = 1

    while q:
        x = q.popleft()

        if x == goal:
            return visited[x] - 1

        for i in (x - d, x + u):
            if 1 <= i <= f and visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1

    return "use the stairs"

print(bfs(s, g))
