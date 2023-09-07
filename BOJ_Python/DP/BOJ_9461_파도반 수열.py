import sys

t = int(sys.stdin.readline())

def pado(n):
    li = [1,1,1]
    for i in range(3, n):
        li.append(li[i-3] + li[i-2])
    return li[n-1]


for i in range(t):
    n = int(sys.stdin.readline())
    if n <= 3:
        print(1)
    else: 
        print(pado(n))