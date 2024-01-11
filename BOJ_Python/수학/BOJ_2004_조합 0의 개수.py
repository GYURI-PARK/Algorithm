# 2의 배수 개수와 5의 배수 개수 중 더 작은게 10의 배수의 개수
import sys
n, k = map(int, sys.stdin.readline().split())

def count(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt
  
five = count(n, 5) - count(k, 5) - count(n-k, 5)
two = count(n, 2) - count(k, 2) - count(n-k, 2)

res = min(five, two)
print(res)