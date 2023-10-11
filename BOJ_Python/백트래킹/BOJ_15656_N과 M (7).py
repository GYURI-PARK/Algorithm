import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

res = []

def backtracking(depth):
    if depth == m:
        set(res)
        print(' '.join(map(str, res)))
        return
    for i in range(n):
        res.append(li[i])
        backtracking(depth+1)
        res.pop()

backtracking(0)