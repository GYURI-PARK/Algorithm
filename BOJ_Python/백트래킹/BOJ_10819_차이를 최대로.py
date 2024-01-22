import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

visited = [False] * n
tmp = []
res = 0

def backtracking(depth):
    global res

    if depth == n:
        print('tmp : ', tmp)
        ans = 0
        for i in range(n-1):
            ans += abs(li[tmp[i]] - li[tmp[i+1]])
        res = max(res, ans)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            tmp.append(i)
            backtracking(depth+1)
            visited[i] = False
            tmp.pop()

backtracking(0)
print(res)