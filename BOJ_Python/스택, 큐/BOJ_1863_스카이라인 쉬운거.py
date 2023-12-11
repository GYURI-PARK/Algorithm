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
#     elif y < stack[-1] and y in stack:
#         stack.pop()

# print(res)

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    while len(stack) > 0 and stack[-1] > y:
        res += 1
        print('res', res)
        stack.pop()
    if len(stack) > 0 and stack[-1] == y:
        continue
    stack.append(y)
    print('stack', stack)

while len(stack) > 0:
    if stack[-1] > 0:
        res += 1
    stack.pop()

print(res)

# y가 변하는 지점들을 확인하면서 stack에 넣거나 뺀다.
# y가 같다면 stack에 넣지 않고, stack의 top보다 작으면 건물의 개수(answer)를 1씩 증가시킨다.
# 마지막으로 stack에 남아 있는 값들을 꺼내면서 0보다 크면 건물의 개수를 1씩 증가시킨다.