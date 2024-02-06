import sys

s, p = map(int, sys.stdin.readline().split())
dna = sys.stdin.readline().rstrip()
a,c,g,t = map(int, sys.stdin.readline().split())

res = 0
dic = {'A': 0, 'C':0, 'G':0, 'T':0}

start = 0
end = p - 1

arr = dna[start:end]

for ii in arr:
    dic[ii] += 1

while end < s:
    dic[dna[end]] += 1
    if dic["A"] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] > t:
        res += 1
    dic[dna[start]] -= 1
    start += 1
    end += 1

print(res)