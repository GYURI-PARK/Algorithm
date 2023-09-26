import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
visited = [False] * n
box = []

li.sort()

def backtracking(depth):
    if depth == m:
        print(' '.join(map(str, box)))
        return
    tmp = 0
    for i in range(n):
        if not visited[i] and tmp != li[i]:
            visited[i] = True
            box.append(li[i])   
            tmp = li[i]
            backtracking(depth + 1)
            visited[i] = False
            box.pop()
backtracking(0)