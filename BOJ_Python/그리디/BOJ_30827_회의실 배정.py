import sys

n, k = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

li.sort(key=lambda x:[x[0], x[1]])

room = [[0] for _ in range(k)]
res = 0

for i in range(n):
    for j in range(k):
        if room[j][-1] < li[i][0]:
            room[j].append(li[i][1])
            res += 1
            break
# print(room)
# print(res)


print(res)