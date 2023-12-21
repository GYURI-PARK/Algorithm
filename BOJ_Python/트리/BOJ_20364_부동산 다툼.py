import sys

n, q = map(int, sys.stdin.readline().split())
graph = [int(sys.stdin.readline()) for _ in range(q)]

visited = set()

for i in range(q):
    res = 0
    duck = graph[i]

    while duck > 1:
        if duck in visited:
            res = duck
        duck //= 2
    visited.add(graph[i])

    print(res)
