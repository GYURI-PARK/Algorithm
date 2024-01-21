import sys

s, p = map(int, sys.stdin.readline().split())
dna = sys.stdin.readline().rstrip()
a, c, g, t = map(int, sys.stdin.readline().split())

start, end = 0, p-1
cnt = 0

dic = {'A':0, 'C':0, 'G':0, 'T':0}
arr = dna[start:end]
for i in arr:
    dic[i] += 1

while end < s:
    dic[dna[end]] += 1
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt += 1

    dic[dna[start]] -= 1
    start += 1 
    end += 1

print(cnt)