import sys

n, x = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

tmp = sum(li[:x])
res = tmp
cnt = 1

for i in range(x, n):
    tmp -= li[i-x]
    tmp += li[i]
    if res < tmp:
        res = tmp
        cnt = 1
    elif res == tmp:
        cnt += 1

if res == 0:
    print("SAD")
else:
    print(res)
    print(cnt)