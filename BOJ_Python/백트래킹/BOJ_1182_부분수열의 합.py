import sys

n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
cnt = 0
ans = []

def backtracking(depth):
    global cnt

    if len(ans) > 0 and sum(ans) == s:
        cnt += 1
        print('ans', ans)
        
    for i in range(depth, n):
        ans.append(li[i])
        backtracking(i+1)
        ans.pop()

backtracking(0)
print(cnt)