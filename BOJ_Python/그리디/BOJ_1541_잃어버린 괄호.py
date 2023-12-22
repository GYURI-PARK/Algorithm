import sys

input = sys.stdin.readline().rstrip()
tmp = input.split('-')
li = []

for i in tmp:
    sum = 0
    sum_tmp = i.split('+')
    for j in sum_tmp:
        sum += int(j)
    li.append(sum)

res = li[0]
for i in range(1, len(li)):
    res -= li[i]

print(res)