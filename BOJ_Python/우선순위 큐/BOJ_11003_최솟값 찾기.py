import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

q = deque()
res = []

for i in range(n):
    while q and q[-1][0] > li[i]:
        q.pop()
    while q and q[0][1] < i - l + 1:
        q.popleft()
    q.append((li[i], i))
    print(q[0][0])