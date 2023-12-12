import sys
from itertools import combinations

input = list(sys.stdin.readline().rstrip())
stack = []
ans = []
indices = [] # 괄호들의 위치 (쌍으로)

for i in range(len(input)):
    if input[i] == "(":
        stack.append(i)
    elif input[i] == ")":
        indices.append((stack.pop(), i))

for i in range(len(indices)):
    for comb in combinations(indices, i+1):
        temp = input[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
        ans.append("".join(temp))

ans = set(ans)
ans = sorted(list(ans))

for i in ans:
    print(i)