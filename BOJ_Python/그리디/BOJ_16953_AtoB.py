import sys

a,b = map(int, sys.stdin.readline().split())

# 짝수면 나누기 2
# 1로 끝나면 오른쪽 1빼기
cnt = 1

# 시간초과 코드
# while a < b:
#     if b % 2 == 0:
#         b = b // 2
#         cnt += 1
#     elif str(b)[len(str(b))-1] == '1':
#         b = int(str(b)[0:len(str(b))-1])
#         cnt += 1
    
# if a == b:
#     print(cnt+1)
# else:
#     print(-1)
    
while True:
    if a == b:
        break
    elif a > b:
        cnt = -1
        break
    elif b % 2 ==0:
        b = b // 2
        cnt += 1
    elif str(b)[len(str(b))-1] == '1':
        b = int(str(b)[0:len(str(b))-1])
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)
        
