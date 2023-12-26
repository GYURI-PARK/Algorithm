import sys

n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())
    li = [1,1]
    cnt = 1
    idx = 2
    while cnt < num:
        cnt = li[idx-2] + li[idx-1]
        idx += 1
        li.append(cnt)
    res = []
    for i in range(len(li)):
        if li[len(li)-1-i] <= num:
            res.append(li[len(li)-1-i])
            num -= li[len(li)-1-i]
    
    res.reverse()
    print(*res)