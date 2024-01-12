import sys
from itertools import product

n, k = map(int, sys.stdin.readline().split())
li = list(sys.stdin.readline().split())
li.sort(reverse=True)
length = len(str(n))

while True:
    res = list(product(li, repeat = length))
    for i in res:
        tmp = ''.join(i)
        if int(tmp) <= n:
            print(tmp)
            exit()
    length -= 1