import sys

n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False] * n
tmp = []
res = 1e9

def dfs(idx, depth):
    global res
    
    if tmp:
        print('tmp : ', tmp)
        ans = 0
        s = 1
        b = 0
        for i in tmp:
            s *= li[i][0]
            b += li[i][1]
            ans = abs(s-b)
        res = min(res, ans)
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            tmp.append(i)
            dfs(i, depth+1)
            visited[i] = False
            tmp.pop()
dfs(0,0)
print(res)
