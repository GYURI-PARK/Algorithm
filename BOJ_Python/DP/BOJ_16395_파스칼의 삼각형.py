# 이항계수 공식 = n! / (k! * (n-k)!)

n,k = map(int, input().split())

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    

print(int(fact(n-1) / (fact(k-1) * fact(n-k))))