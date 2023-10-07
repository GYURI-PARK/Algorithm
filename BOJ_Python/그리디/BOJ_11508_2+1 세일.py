import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))


li.sort(reverse=True)
res = 0 

for i in range(n):
    if (i+1) % 3 == 0:
        continue
    else:
        res += li[i]

print(res)