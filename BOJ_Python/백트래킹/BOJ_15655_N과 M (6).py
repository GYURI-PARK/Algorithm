import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
box = []
li.sort()

def backtracking(depth):
    if len(box) == m:
        print(' '.join(map(str, box)))
        return

    for i in range(depth, n):
        if li[i] in box:
            continue
        box.append(li[i])  
        backtracking(i)
        box.pop()

backtracking(0)