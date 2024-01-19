import sys

ans = list(map(int, sys.stdin.readline().split()))
res = 0
tmp = []

def backtracking(depth):
    global res

    if depth == len(ans):
        score = 0
        for j in range(10):
            if tmp[j] == ans[j]:
                score += 1
        if score >= 5:
            res += 1
        return
    
    # 5지선다
    for i in range(1, 6):
        if depth > 1 and tmp[depth-2] == tmp[depth-1] == i:
            continue
        tmp.append(i)
        backtracking(depth+1)
        tmp.pop()

backtracking(0)
print(res)
