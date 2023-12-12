import sys

input = sys.stdin.readline().rstrip()

stack = []
cnt = 0

for i in range(len(input)):
    if input[i] == "(":
        stack.append("(")
    else:
        if input[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)