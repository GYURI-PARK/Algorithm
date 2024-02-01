import sys

n,m = map(int, sys.stdin.readline().split())
ex = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
test = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

tmp = []
tmp_val = 0
for i in range(n):
    tmp_val += ex[i][0]
    tmp.append(tmp_val)
    
li = [0] * (101)
idx = 0
while idx < n-1:
    for i in range(1, 101):
        if i <= tmp[idx]:
            li[i] += ex[idx][1]
        else:
            li[i] += ex[idx+1][1]
            idx += 1

test_tmp = []
test_val = 0
for i in range(m):
    test_val += test[i][0]
    test_tmp.append(test_val)
test_li = [0] * (101)
idx = 0
while idx < m-1:
    for i in range(1, 101):
        if i <= test_tmp[idx]:
            test_li[i] += test[idx][1]
        else:
            test_li[i] += test[idx+1][1]
            idx += 1

res = 0
for i in range(1, 101):
    if test_li[i] > li[i]:
        res = max(res, abs(test_li[i] - li[i]))

print(res)