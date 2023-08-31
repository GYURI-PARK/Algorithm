import sys

x, y = map(int, sys.stdin.readline().split())
z =  (y  * 100) // x

if z >= 99:
    print(-1)
else: 
    start = 1
    end = x
    res = 0

    while start <= end:
        mid = (start + end) // 2
        if ((y + mid) * 100) // (x + mid) <= z:
            start = mid + 1
        else:
            res = mid
            end = mid -1 
    print(res)