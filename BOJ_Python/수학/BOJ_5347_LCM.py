import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li1 = []
    li2 = []

    for j in range(2, a+1):
        if a % j == 0:
            li1.append(j)
    for k in range(2, b+1):
        if b % k == 0:
            li2.append(k)

    li = set(li1) & set(li2)

    if len(li) != 0:
        print(max(li) * (a // max(li)) * (b // max(li)))
    else:
        print(a * b)
    


import sys
from math import lcm

for _ in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split())
    print(lcm(a,b))
