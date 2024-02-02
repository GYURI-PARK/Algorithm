import sys
from collections import deque

n = int(sys.stdin.readline())
li = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    li.append((a,b))

li.sort(key=lambda x:[x[1],x[0]])
# print(li)

res = 0
q = [0]
for i in range(n):
    if li[i][0] >= q[-1]:
        q.append(li[i][1])
        res += 1
    else:
        continue

print(res)

