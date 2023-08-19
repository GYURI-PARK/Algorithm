# O(N제곱logN) 풀이 : k, l 2중 for문, a[l]-a[k]가 배열 two에 있는지 이분탐색
# x + y + z = k -> x + y = k - z

import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()

two = []
for i in range(n):
    for j in range(i, n):
        two.append(li[i]+li[j])
two.sort()
res = 0
for i in range(n):
    for j in range(i, n):
        a = li[j] - li[i]
        start = 0
        end = len(two) - 1
        while start <= end:
            mid = (start + end) // 2
            b = two[mid]
            if a > b:
                start = mid + 1
            elif a < b:
                end = mid - 1
            else:
                res = max(res, li[j])
                break


print(res)