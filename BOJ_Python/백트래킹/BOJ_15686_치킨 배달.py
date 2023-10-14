import sys

n, m = map(int, sys.stdin.readline().split())
house = []
chicken = []
res = int(1e9)

for i in range(n):
    graph = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if graph[j] == 1:
            house.append((i, j))
        elif graph[j] == 2:
            chicken.append((i, j))

visited = [False] * len(chicken)

def backtracking(depth, idx):
    global res, distance
    
    if depth == m:
        tmp = 0
        for i in house:
            distance = int(1e6)
            for j in range(len(visited)):
                if visited[j]:
                    distance = min(distance, abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1]))
            tmp += distance
        res = min(res, tmp)
        return
    
    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1, idx+1)
            visited[i] = False

backtracking(0,0)
print(res)
