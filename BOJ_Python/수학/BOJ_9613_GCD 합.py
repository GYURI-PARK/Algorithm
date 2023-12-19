import sys

t = int(sys.stdin.readline())

# 최대공약수
def GCD(a, b):
    if b % a == 0:
        return a
    else:
        return GCD(b%a, a)
    
for i in range(t):
    res = 0
    li = list(map(int, sys.stdin.readline().split()))
    # li[0] = 정수 개수
    idx = 1
    while idx < li[0]+1:
        for j in range(idx, li[0]):
            res += GCD(li[idx], li[j+1])
        idx += 1

    print(res)
