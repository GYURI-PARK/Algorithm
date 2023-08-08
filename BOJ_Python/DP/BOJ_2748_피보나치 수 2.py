# 시간초과
# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fibo(n-1) + fibo(n-2)
    

# n = int(input())
# print(fibo(n-1))

# --------------------
fibo = []
n = int(input())

for i in range(n+1):
    if i == 0:
        fibo.append(0)
    elif i == 1:
        fibo.append(1)
    else:
        fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[n])