import sys

e,s,m = map(int, sys.stdin.readline().split())
res = 1

while True:
    if (res-e) % 15 == 0 and (res-s) % 28 == 0 and (res-m) %  19 == 0:
        break
    res += 1
print(res)
    
    