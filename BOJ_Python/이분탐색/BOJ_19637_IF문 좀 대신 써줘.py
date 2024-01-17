import sys

n, m = map(int, sys.stdin.readline().split())
# li = [list(sys.stdin.readline().split()) for _ in range(n)]

li = []

for i in range(n):
    a, b = sys.stdin.readline().split()
    li.append([a, int(b)])

li.sort(key=lambda x : x[1])

for i in range(m):
    num = int(sys.stdin.readline())
    start, end = 0, len(li)-1

    while start <= end:
        mid = (start + end) // 2
        if num > li[mid][1]:
            start = mid + 1
        else:
            end = mid - 1
    print(li[start][0])