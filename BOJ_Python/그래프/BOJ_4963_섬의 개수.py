import sys
sys.setrecursionlimit(10**6)  

dx = [0,0,-1,1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]

def dfs(depth, x, y):
    global cnt

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < h and -1 < ny < w:
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(depth+1, nx, ny)
    return

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        quit()
    
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(1, i, j)
                cnt += 1
    print(cnt)

