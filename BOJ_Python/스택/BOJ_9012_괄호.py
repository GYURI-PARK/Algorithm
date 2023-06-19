import sys

n = int(sys.stdin.readline())

for i in range(n) :
    stack = []
    s = sys.stdin.readline()
    for i in s :
        if i == "(":
            stack.append(i)
        elif i == ")" :
            if len(stack) == 0:
                print("NO")
                break
            else: 
                stack.pop()

    else :
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")