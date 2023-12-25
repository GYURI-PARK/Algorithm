import sys

l, r = sys.stdin.readline().split()
res = 0

if len(l) != len(r): 
    print(0)
else:
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                res += 1
        else:
            break
    print(res)
