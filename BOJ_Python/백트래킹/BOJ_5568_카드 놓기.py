import sys
import itertools 

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
s = []

for i in range(n):
    s.append(int(sys.stdin.readline()))

nPk = list(itertools.permutations(s, k))

res = []
for i in range(len(nPk)):
    tmp = ""
    for j in range(k):
        tmp += str(nPk[i][j])
    res.append(tmp)

print(len(set(res)))

# 백트레킹으로 풀어보자 !

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
s = []

for i in range(n):
    s.append(sys.stdin.readline().rstrip())

check = [0] * n
tmp = []
res = set()

def card(N):
    if N == k:
        res.add(''.join(tmp))
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = 1
        tmp.append(s[i])

        card(N+1)

        check[i] = 0
        tmp.pop()
card(0)
print(len(res))