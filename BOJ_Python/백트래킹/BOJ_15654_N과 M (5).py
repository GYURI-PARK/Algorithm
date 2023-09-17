# import sys
# import itertools

# # 순열 : itertools.permustations(li, n)
# n, m = map(int, sys.stdin.readline().split())
# li = list(map(int, sys.stdin.readline().split()))

# nPr = list(itertools.permutations(li, m))
# nPr.sort()

# for i in range(len(nPr)):
#     for x in nPr[i]:
#         print(x, end = ' ')
#     print('')



# 백트레킹

import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
box = []

li.sort()


def backtracking(depth):
    if depth == m:
        print(' '.join(map(str, box)))
        return
    for i in range(n):
        if li[i] in box:
            continue
        box.append(li[i])
        backtracking(depth + 1)
        box.pop()

backtracking(0)
