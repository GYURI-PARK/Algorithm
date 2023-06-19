## 자료구조 스택
### BOJ_2493_탑

import sys

n = int(sys.stdin.readline()) 

tower = list(map(int, sys.stdin.readline().split()))
stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][1] >= tower[i]:
            result.append(stack[-1][0]+1) 
            break
        else: stack.pop()

    if not stack:
        result.append(0) 
    
    stack.append((i, tower[i])) 

for i in result:
    print(i, end = ' ')
