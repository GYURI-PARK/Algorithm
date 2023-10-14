import sys

def backtracking(depth, idx):
    if depth == 6:
        print(' '.join(map(str, res)))
        return
    for i in range(idx, k):
        res.append(s[i+1])
        backtracking(depth+1, i+1)
        res.pop()
        

while True:
    s = list(map(int, sys.stdin.readline().split()))
    k = s[0]
    res = []
    if k == 0:
        break
    backtracking(0,0)
    print()
