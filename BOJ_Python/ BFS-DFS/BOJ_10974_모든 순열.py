# 순열 
from itertools import permutations

n = int(input())
for i in permutations([j for j in range(1, n+1)]):
    print(*i)


# DFS
n = int(input())
graph = [i for i in range(1, n+1)]
tmp = []

def dfs(depth):
    if depth == n:
        print(*tmp)
        return 
    
    for i in range(n):
        if graph[i] not in tmp:
            tmp.append(graph[i])
            dfs(depth+1)
            tmp.pop()