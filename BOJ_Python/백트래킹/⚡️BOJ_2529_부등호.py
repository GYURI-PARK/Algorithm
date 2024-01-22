import sys

k = int(sys.stdin.readline())
li = list(sys.stdin.readline().split())

min_res = ''
max_res = ''

visited = [False] * 10


def check(mark, a, b):
    if mark == "<":
        return a < b
    else:
        return a > b

def dfs(depth, s):
    global min_res, max_res

    if depth == k+1:
        if len(min_res) == 0:
            min_res = s
        else:
            max_res = s
        return
    
    for i in range(10):
        if not visited[i]:
            if  depth == 0 or check(li[depth-1], s[-1], str(i)):
                visited[i] = True
                dfs(depth+1, s+str(i))
                visited[i] = False

    
dfs(0, '')
print(max_res)
print(min_res)