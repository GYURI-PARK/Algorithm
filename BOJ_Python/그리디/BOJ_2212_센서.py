import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()

li = []

for i in range(0, n-1):
    li.append(sensor[i+1]-sensor[i])

res = 0
li.sort()

for i in range(n-k):
    res += li[i]

print(res)
