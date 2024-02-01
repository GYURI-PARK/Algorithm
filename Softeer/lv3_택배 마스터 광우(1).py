import sys
from itertools import permutations

n,m,k = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))

li = permutations(weight, n)
res = sys.maxsize

for i in li:
    cnt = 0 # 일의 시행 횟수
    sum_tmp = 0 # (5+10) + (8) + (19) + (7+5)
    idx = 0 # 0,1,2,3,4
    tmp = 0 # 5 + 8 
    ii = list(i)
    while cnt != k:
        if tmp + ii[idx] <= m:
            tmp += ii[idx]
            ii.append(ii[idx])
            idx += 1
        else:
            sum_tmp += tmp
            tmp = 0
            cnt += 1
    res = min(res, sum_tmp)
    
print(res)