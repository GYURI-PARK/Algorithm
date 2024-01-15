import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

dic = dict()

for i in range(t):
    if len(dic) == n and num[i] not in dic.keys():
        keys = list(dic.keys())
        values = list(dic.values())
        tmp = values.index(min(values))
        idx = keys[tmp]
        del(dic[idx])
    if num[i] in dic.keys():
        dic[num[i]] += 1
    if num[i] not in dic.keys():
        dic[num[i]] = 1

res = list(dic.keys())
res.sort()
print(*res)