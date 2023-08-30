# import sys
# from collections import deque

# r, c = map(int, sys.stdin.readline().split())
# graph = []

# # for i in range(r):
# #     graph.append(list(sys.stdin.readline().rstrip()))
# fire = [[0] * r for _ in range(c)]
# jihoon = [[0] * r for _ in range(c)]

# for i in range(r):
#     graph.append(list(sys.stdin.readline().rstrip()))
#     for j in range(c):
#         if graph[i][j] == "J":
#             jihoon[i][j] = 1
#         elif graph[i][j] == "F":
#             fire[i][j] = 1

# q_fire = deque()
# q_jihoon = deque()

# dx = [0,0,-1,1]
# dy = [1,-1,0,0]     

# fire = [[0] * r for _ in range(c)]
# jihoon = [[0] * r for _ in range(c)]

# for i in range(r):
#     for j in range(c):
#         if graph[i][j] == "F":
#             q_fire.append((i,j))
#         if graph[i][j] == "J":
#             q_jihoon.append((i,j))
#             jihoon[i][j] = 1

# while q_fire:
#     tmp = q_fire.popleft()
#     for k in range(4):
#         nx = tmp[0] + dx[k]
#         ny = tmp[1] + dy[k]

#         if nx < 0 or nx >= r or ny < 0 or ny >= c:
#             continue
#         if graph[nx][ny] == "#" :
#             continue
#         if graph[nx][ny] == "." or graph[nx][ny] == "F":
#             fire[nx][ny] = fire[tmp[0]][tmp[1]] + 1
#             q_fire.append((nx,ny))

# print(fire)

import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def fbfs():
    while fq:
        r, c = fq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if maze[nr][nc] == "#" or fire[nr][nc]:
                continue
            fire[nr][nc] = fire[r][c] + 1
            fq.append((nr, nc))

def hbfs():
    while hq:
        r, c = hq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                print(human[r][c])
                return
            if human[nr][nc] or maze[nr][nc] == "#":
                continue
            if fire[nr][nc] and human[r][c] + 1 >= fire[nr][nc]:
                continue
            human[nr][nc] = human[r][c] + 1
            hq.append((nr, nc))
    print("IMPOSSIBLE")
    return

# main
R, C = map(int, input().split())
maze = []
hq = deque()
fq = deque()
human = [[0] * C for _ in range(R)]
fire = [[0] * C for _ in range(R)]
for i in range(R):
    maze.append(list(input().strip()))
    for j in range(C):
        if maze[i][j] == "J":
            hq.append((i, j))
            human[i][j] = 1
        elif maze[i][j] == "F":
            fq.append((i, j))
            fire[i][j] = 1
fbfs()
hbfs()