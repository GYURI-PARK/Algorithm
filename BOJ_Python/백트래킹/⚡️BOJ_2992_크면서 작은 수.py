import sys

x = int(sys.stdin.readline())
res = ''
minNum = '999999'
visited = [False] * len(str(x))

def backtracking(depth):
    global res 
    global minNum

    if depth == len(str(x)):
        if x < int(res) < int(minNum):
            minNum = res
        return

    for i in range(len(str(x))):
        if not visited[i]:
            visited[i] = True
            res += str(x)[i]
            backtracking(depth+1)
            res = res[:-1]
            visited[i] = False

backtracking(0)
if minNum == '999999':
    print(0)
else:
    print(minNum)
