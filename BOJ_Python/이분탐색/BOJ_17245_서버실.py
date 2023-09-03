# max = 입력받은 수 중 가장 큰 값
# 

# n = int(input())
# li = []
# res = 0 
# computer = 0 # 

# for i in range(n):
#     tmp = list(map(int, input().split()))
#     li.append(tmp)
#     computer += sum(tmp)


# # coumputer * 0.5 보다 더 많이 정상 작동 해야됨


# start, end = 0, max(li)
# print(end)

def count(li, m, N):
    t = 0
    for i in range(N):
        for j in range(N):
            t += (m if m <= li[i][j] else li[i][j])
    return t

N = int(input())
li = []
max_li = sum_li = 0
for _ in range(N):
    a = list(map(int, input().split()))
    li.append(a)
    max_li = max(max_li, max(a))
    sum_li += sum(a)
s, e = 0, max_li
res = 0
while s <= e:
    m = (s+e)//2
    if count(li, m, N) >= sum_li/2:
        res = m
        e = m-1
    else:
        s = m+1
print(res)

## #############

import sys

input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
sm = 0
mx = 0
for i in range(n):
    for j in range(n):
        sm += li[i][j]
        mx = max(mx, li[i][j])
left = 0
right = mx
temp = [] # 조건에 만족하는 경우를 모두 저장해두고, 여기서 min값을 뽑으면 될 듯 !
while left <= right:
    mid = (left + right) // 2
    ans = 0
    for i in range(n):
        for j in range(n):
            if li[i][j] >= mid:
                ans += mid
            else:
                ans += li[i][j]
    if sm/2 > ans: # sm/2 <= ans을 찾는 게 목표
        left = mid + 1
    else:
        temp.append(mid)
        right = mid - 1
print(min(temp))
