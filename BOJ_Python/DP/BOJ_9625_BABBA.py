# 한번 눌렀을 때 a = 0, b = 1
# 두번째 눌렀을 때, a = 1, b = 1 -> a = 1, b = 2 -> a = 2, b = 3 

K = int(input())
a,b = 0,1
for i in range(1,K):
    a, b = b, a+b
print(a,b)