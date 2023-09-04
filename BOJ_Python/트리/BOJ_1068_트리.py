import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline())

def dfs(node, arr):
    # 삭제할 노드 값 -2로 갱신
    arr[node] = -2
    for i in range(len(arr)):
        if node == arr[i]:
            dfs(i, arr)

cnt = 0
dfs(delete, li)
for i in range(len(li)):
    # 삭제될 노드도 아니면서 다른 노드의 부모노드가 아닌 원소
    if li[i] != -2 and i not in li:
        cnt += 1

print(cnt)
