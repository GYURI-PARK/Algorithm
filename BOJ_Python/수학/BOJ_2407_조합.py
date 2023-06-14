# 💡 조합공식 : n! / (n-r)!*r!

# 1.

def fac(n):
    num = 1
    for i in range(2,n+1):
        num*=i
    return num

n,m = map(int,input().split())
print(fac(n) // (fac(m)*fac(n-m)))


# 2.
import math

n, m = map(int, input().split())

numer = math.factorial(n)
deno = (math.factorial(n-m)) * (math.factorial(m))

print(numer//deno)