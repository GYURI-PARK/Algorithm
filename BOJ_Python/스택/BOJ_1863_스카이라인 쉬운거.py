import sys

# y가 stack에 없으면 추가하고 res += 1
# y < stack[-1] 이면 stack.pop()
n = int(sys.stdin.readline())

stack = []
res = 0

# for i in range(n):
#     x, y = map(int, sys.stdin.readline().split())
    
#     if y not in stack and y != 0:
#         stack.append(y)
#         res += 1
#     elif y < stack[-1]:
#         stack.pop()

# print(res)

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    while len(stack) > 0 and stack[-1] > y:
        res += 1
        stack.pop()
    if len(stack) > 0 and stack[-1] == y:
        continue
    stack.append(y)

while len(stack) > 0:
    if stack[-1] > 0:
        res += 1
    stack.pop()

print(res)