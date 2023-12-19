import sys

# a,b,l = map(int, sys.stdin.readline().split())
# dic = dict()

# # 소인수분해
# def soinsu(num):
#     res = []
#     i = 2
#     while i <= num:
#         if num % i == 0:
#             res.append(i)
#             num = num / i
#         else:
#             i += 1
#     return res

# a_soinsu = soinsu(a)
# b_soinsu = soinsu(b)

# # 소인수 -> dictionary
# def toDict(li, dic):
#     for i in range(len(li)):
#         if li[i] in dic:
#             dic[li[i]] += 1
#         else:
#             dic[li[i]] = 1
#     return dic

# dic = toDict(a_soinsu, dic)
# dic = toDict(b_soinsu, dic)

# l_soinsu = soinsu(l)
# res_dic = toDict(l_soinsu, dict())

# ans = 1

# for i in res_dic:
#     if a * b == l:
#         ans = 1
#     elif l % (a * b) == 0:
#         ans = l // (a * b) 
#     elif i in dic.keys() and res_dic[i] > dic[i]-1:
#         ans *= i ** res_dic[i]
#     elif i not in dic.keys() and l % (a*b) == 0:
#         ans *= i ** res_dic[i]
#     elif i not in dic.keys() and l % (a*b) != 0:
#         ans = -1
        
# print(ans)

# 최대 공약수
def GCD(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

# 최소 공배수 
def LCM(a, b):
    return (a // GCD(a, b)) * b

# 약수
def Divisor(num, li):
    for i in range(1, int(num**(0.5) + 1)):
        if num % i == 0:
            li.append(i)
            if i * i != num and i * i <= num:
                li.append(num // i)
    return li

a, b, l = map(int, sys.stdin.readline().split())
l_list = []
Divisor(l, l_list)
l_list.sort()
lcm = LCM(a, b)

res = -1
for i in range(len(l_list)):
    if LCM(lcm, l_list[i]) == l:
        res = l_list[i]
        break

print(res)