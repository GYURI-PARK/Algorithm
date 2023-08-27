import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
cnt = 0

li.sort()

left = 0
right = n - 1

while left < right:
    sum = li[left] + li[right]
    if sum < m:
        left += 1
    elif sum > m:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)