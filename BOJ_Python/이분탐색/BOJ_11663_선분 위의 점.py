import sys

n,m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

def dot_min(a):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if li[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return start

def dot_max(b):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if b < li[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dot_max(b) - dot_min(a) + 1)

