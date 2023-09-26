import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
box = []

a = list(set(li))
b = sorted(a)

def backtracking(depth):
    if len(box) == m:
        print(' '.join(map(str, box)))
        return
    for i in range(depth, len(b)):
        box.append(b[i])  
        backtracking(i)
        box.pop()
backtracking(0)