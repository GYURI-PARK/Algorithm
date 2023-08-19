import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
order = sorted(num)
m = int(sys.stdin.readline())
M = map(int, sys.stdin.readline().split())

def binarySearch(N, target, start, end):
    mid = (start + end) // 2

    if start > end:
        return 0
    if target == N[mid]:
        return 1
    elif target < N[mid]:
        return binarySearch(N, target, start, mid-1)
    else:
        return binarySearch(N, target, mid+1, end)

for i in M:
    start = 0 
    end = len(num) - 1
    print(binarySearch(order, i, start, end))
