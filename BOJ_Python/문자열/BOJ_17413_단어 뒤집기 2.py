import sys

s = sys.stdin.readline().rstrip() + ' '
tmp = []
res = ''
# 괄호 안에 있는지 여부 판단
isInside = 0

for i in range(len(s)):
    if s[i] == '<':
        isInside = 1
        for j in range(len(tmp)):
            res += tmp.pop()
    tmp.append(s[i])
    
    if s[i] == '>':
        isInside = 0
        for j in range(len(tmp)):
            res += tmp.pop(0)
    if s[i] == ' ' and isInside == 0:
        tmp.pop()
        for j in range(len(tmp)):
            res += tmp.pop()
        res += ' '

print(res)