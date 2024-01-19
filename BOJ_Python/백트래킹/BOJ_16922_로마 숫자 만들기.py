import sys

n = int(sys.stdin.readline())
li = [1, 5, 10, 50]
res = []

def backtracking(depth, tmp, idx):
    global res

    if depth == n:
        if tmp not in res:
            res.append(tmp)
        return 
    
    for i in range(idx, 4):
        tmp += li[i]
        backtracking(depth+1, tmp, i)
        tmp -= li[i]

backtracking(0,0,0)
print(len(res))