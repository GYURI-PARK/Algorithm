# 시간초과

# import sys 

# n,k = map(int, sys.stdin.readline().split())
# li = list(map(int, sys.stdin.readline().split()))

# left, right = 0, 1
# cnt = 0 # 라이언의 수
# ans = 0 # k개의 라이언이 포함된 배열의 길이

# while right <= n and left <= right:
#     cnt = li[left:right].count(1)
#     if cnt < k:
#         right +=1 
#     elif cnt == k and ans == 0:
#         ans = len(li[left:right])
#         left += 1
#     elif cnt == k and ans != 0:
#         ans = min(len(li[left:right]), ans)
#         left += 1
# print(ans)

# 필요한 부분만 탐색
import sys 

n,k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
cnt = 0 # 라이언의 수
ans = 1000000 # k개의 라이언이 포함된 배열의 길이

while right < n:
    if li[right] == 1:
        cnt += 1
    while cnt == k:
        ans = min(ans, right-left+1)
        if li[left] == 1:
            cnt -= 1
        left += 1
    right += 1

if ans == 1000000:
    print(-1)
else:
    print(ans)