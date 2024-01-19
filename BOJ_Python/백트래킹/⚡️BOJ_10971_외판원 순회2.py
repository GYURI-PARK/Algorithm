import sys

n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False] * n 

# 1번부터 시작할 때, 2번부터 시작할때 ... 다 비교해서 최솟값
res = []
def backtracking(depth, index, min_distance, start):
    if depth == n:
        # 시작도시로 갈 수 있는 경우
        if w[index][start] != 0:
            min_distance += w[index][start]
            res.append(min_distance)
        return 
    visited[start] = True
    for i in range(n):
        if visited[i] == False:
            if w[index][i] != 0:
                visited[i] = True
                min_distance += w[index][i]
                backtracking(depth+1, i, min_distance, start)
                visited[i] = False
                min_distance -= w[index][i]


for i in range(n):
    backtracking(1,i,0,i)

print(res)
