sen = list(input())
stack = []
res = 0
tmp = 1

for i in range(len(sen)):
    if sen[i] == '(':
        stack.append(sen[i])
        tmp *= 2
    elif sen[i] == '[':
        stack.append(sen[i])
        tmp *= 3

    elif sen[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if sen[i-1] == '(':
            res += tmp
        stack.pop()
        tmp //= 2

    elif sen[i] == ']':
        if not stack or stack[-1] == '(':
            res = 0
            break
        if sen[i-1] == '[':
            res += tmp
        stack.pop()
        tmp //= 3
        
if stack:
    res = 0

print(res)
