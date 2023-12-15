import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

for i in range(n-1):
    num[i+1] += num[i]

num = [0] + num

for k in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(num[j]-num[i-1])
