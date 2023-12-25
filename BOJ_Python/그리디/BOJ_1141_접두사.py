import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(sys.stdin.readline().rstrip())

li.sort(key=len)
res = 0

for i in range(n):
    tmp = False
    for j in range(i+1, n):
        if li[i] == li[j][0:len(li[i])]:
            tmp = True
            break
    if not tmp:
        res += 1

print(res)