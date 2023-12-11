import sys

n = int(sys.stdin.readline())
data = list(enumerate((map(int, sys.stdin.readline().split())), start = 1))
index = 0

while data:
    tmp = data.pop(index)
    print(tmp[0], end=' ')
    if tmp[1] < 0 and data:
        index = (index + tmp[1]) % len(data)
    elif tmp[1] > 0 and data:
        index = (index + (tmp[1]-1)) % len(data)


import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for i in range(n):
    tmp = deq.popleft()
    print(tmp[0], end=' ')
    if tmp[1] > 0:
        deq.rotate(-(tmp[1] - 1))
    else:
        deq.rotate(-tmp[1])