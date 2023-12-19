import sys

a,b = map(int, sys.stdin.readline().split())
if b > 10000000:
    b = 10000000
# 소수 판별
def sosu(num):
    # for i in range(2, int(num**(0.5))+1):
    #     if num % i == 0:
    #         return False
    # return True
    
    # 에라토스테네스의 체 적용
    arr = [True for _ in range(num+1)] # 처음에 모든 수가 소수로 초기화
    for i in range(2, int(num**(0.5))+1):
        if arr[i] == True:
            for j in range(i+i, num+1, i):
                arr[j] = False

    return [i for i in range(2, num+1) if arr[i] == True]
    
# 팰린드롬
def palin(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

li = sosu(b)
for i in li:
    if palin(i) and i >= a:
        print(i)
print(-1)