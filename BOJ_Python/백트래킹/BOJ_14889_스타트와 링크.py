import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False for _ in range(n)]
res = int(1e9)

def backtracking(depth, idx):
    global res
    if depth == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    start += (graph[i][j] + graph[j][i])
                elif not visited[i] and not visited[j]:
                    link += (graph[i][j] + graph[j][i])
        res = min(res, abs(start - link))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1, i+1)
            visited[i] = False

backtracking(0,0)
print(res)