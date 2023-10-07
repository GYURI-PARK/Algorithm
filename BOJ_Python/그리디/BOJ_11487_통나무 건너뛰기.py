import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    li.sort()
    res = [[0] for _ in range(n)]
    res[n//2] = li[n-1]

    if (n % 2) != 0:
        tmp = n - 1
        for i in range(1, n//2+1):
            res[n//2 + i] = li[tmp-1]
            res[n//2 - i] = li[tmp-2]
            tmp -= 2
    else:
        tmp = n - 1
        for i in range(1, n//2):
            res[n//2 + i] = li[tmp-1]
            res[n//2 - i] = li[tmp-2]
            tmp -= 2
        res[0] = li[0]

    tmp = abs(res[0] - res[n-1])
    for i in range(n-1):
        if abs(res[i+1] - res[i]) > tmp:
            tmp = abs(res[i+1] - res[i])

    print(tmp)
