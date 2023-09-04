import sys

k = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
# li의 중간값이 항상 루트 노드

graph = [[] for _ in range(k)]

# x : 깊이
def makeTree(x, arr):
    mid = (len(arr) // 2)
    # 해당 깊이에 해당하는 node를 추가
    graph[x].append(arr[mid])
    if len(arr) == 1:
        return
    # 왼쪽 / 오른쪽 서브트리로 나누기
    makeTree(x+1, arr[:mid])
    makeTree(x+1, arr[mid+1:])

makeTree(0, li)

for i in range(k):
    print(*graph[i])
