import sys
sys.setrecursionlimit(10 ** 8)

n, K = map(int, sys.stdin.readline().split())
point = [[] for _ in range(K+1)] 

for i in range(n):
    x,y,k = map(int, sys.stdin.readline().split())
    point[k].append([x,y])

res = 4 * 1e6

# cnt: 포함된 color의 num
def dfs(cnt, minX, minY, maxX, maxY):
    global res

    if cnt > K:
        X = abs(maxX - minX)
        Y = abs(maxY - minY)
        tmp = X * Y
        res = min(res, tmp)
        return

    for nx, ny in point[cnt]:
        NminX = min(nx, minX)
        NmaxX = max(nx, maxX)
        NminY = min(ny, minY)
        NmaxY = max(ny, maxY)

        tmp = abs(NmaxX - NminX) * abs(NmaxY - NminY)

        if tmp < res:
            dfs(cnt+1, NminX, NminY, NmaxX, NmaxY)
            
    
for x,y in point[1]:
    dfs(2, x,y,x,y)
print(res)

