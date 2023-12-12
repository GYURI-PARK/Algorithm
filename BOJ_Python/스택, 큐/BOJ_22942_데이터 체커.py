import sys

n = int(sys.stdin.readline())
circle = []
li = []

for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circle.append((x-r, i))
    circle.append((x+r, i))    
circle.sort()

stack = []

for c in circle:
    if stack:
        if stack[-1][1] == c[1]:
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)

if stack:
    print("NO")
else:
    print("YES")