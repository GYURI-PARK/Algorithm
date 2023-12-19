import sys

n = int(sys.stdin.readline())

# 소수 판별
def sosu(num):
    if num == 1:
        return False
    
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True

# 팰린드롬 판별
def pali(num):
    s = str(num)
    if s == s[::-1]:
        return True
    return False

res = 0

for i in range(n, 1000001):
    if sosu(i) and pali(i):
        res = i
        break

if res == 0:
    print(1003001)
else:
    print(res)
