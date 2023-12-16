import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

left, right = 0, 1
ans = 0

while left <= right and right <= n:
    tmp = sum(li[left:right])
    if tmp == m:
        ans += 1
        right += 1
    elif tmp < m:
        right += 1
    else:
        left += 1

print(ans)