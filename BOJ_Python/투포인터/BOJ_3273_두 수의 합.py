import sys

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

cnt = 0

li.sort()
left = 0
right = n-1
while left < right:
    sum = li[left] + li[right]
    if sum < x:
        left += 1
    elif sum > x:
        right -= 1
    else:
        cnt += 1
        right -= 1
        left += 1

print(cnt)