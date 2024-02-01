import sys

n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    tmp = 0
    for i in range(a, b+1):
        tmp += s[i-1]
    print(format(tmp / (b-a+1), '.2f'))