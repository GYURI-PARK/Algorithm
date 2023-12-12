import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
ans = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and num[stack[-1]] < num[i]:
        ans[stack.pop()] = num[i]
    stack.append(i)

print(*ans)
# print(ans)