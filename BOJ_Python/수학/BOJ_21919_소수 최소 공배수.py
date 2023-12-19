import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

# 소수 판별 함수
def isSosu(num):
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True

res = 1
for i in set(li):
    if isSosu(i):
        res *= i

if res == 1:
    print(-1)
else:
    print(res)
