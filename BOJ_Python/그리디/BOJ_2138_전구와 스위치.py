import sys

n = int(sys.stdin.readline())

prev = list(map(int, sys.stdin.readline().rstrip()))
now = list(map(int, sys.stdin.readline().rstrip()))

def change(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num

def switch(li, cnt):
    count = cnt

    if count == 1:
        li[0] = change(li[0])
        li[1] = change(li[1])
    
    for i in range(1, n):
        if li[i-1] != now[i-1]:
            count += 1
            li[i-1] = change(li[i-1])
            li[i] = change(li[i])
            if i != n-1:
                li[i+1] = change(li[i+1])
    if li == now:
        return count 
    else:
        return -1
    
res1 = switch(prev[:], 0) # 시작할 때 스위치를 누를 경우
res2 = switch(prev[:], 1) # 시작할 때 스위치를 누르지 않을 경우

if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)