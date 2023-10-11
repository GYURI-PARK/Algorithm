import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

res = []

def backtracking(depth):
    if m == depth:
        print(' '.join(map(str, res)))
        return
    tmp = 0
    for i in range(n):
        if tmp != li[i]:
            res.append(li[i])
            tmp = li[i]
            backtracking(depth+1)
            res.pop()
        

backtracking(0)
