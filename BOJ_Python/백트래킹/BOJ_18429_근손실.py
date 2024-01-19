import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

cnt = 0
visited = [False] * n

def backtracking(depth, weight):
    global cnt

    if depth == n:
        cnt += 1
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            weight += (a[i] - k)

            if weight >= 500:
                backtracking(depth+1, weight)

            visited[i] = False
            weight -= (a[i] - k)

backtracking(0, 500)
print(cnt)
