import sys

n, m = map(int, sys.stdin.readline().split())
li = [sys.stdin.readline().rstrip() for _ in range(n)]

res = ''
cnt = 0
for i in range(m):
    dic = {'A':0, 'C':0, 'G':0, 'T':0} 
    for j in range(n):
        if li[j][i] == 'T':
            dic['T'] += 1
        elif li[j][i] == 'A':
            dic['A'] += 1
        elif li[j][i] == 'C':
            dic['C'] += 1
        else:
            dic['G'] += 1
        
    chosen_key = max(dic, key=lambda k: dic[k])
    res += chosen_key

    for j in range(n):
        if li[j][i] != chosen_key:
            cnt += 1
    
print(res)
print(cnt)