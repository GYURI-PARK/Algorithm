import sys

n,m,l = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.append(0)
li.append(l-1)

for i in range(m+1):
    diff = []
   
    sort = sorted(li)
    
    for i in range(0, len(sort)-1):
        diff.append(sort[i+1] - sort[i])
    
    index = diff.index(max(diff))
    start = sort[index]
    end = sort[index + 1]
    
    mid = (start + end) // 2
    
    if max(diff) >= max(sort[len(sort) // 2] - mid, mid - sort[(len(sort) // 2)-1]):
        end = mid - 1
    else:
        start = mid + 1

    li.append(mid)
    print(diff)
   
print(max(diff))

# ==========

import sys

n,m,l = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

data.append(0)
data.append(l-1)
data.sort()

start = 0
end = data[-1]
while start <= end:
    cnt = 0
    mid  = (start+end) // 2
    for i in range(1,len(data)):
        if (data[i]-data[i-1]) > mid:
            cnt += (data[i]-data[i-1] - 1)//mid
    
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)


# ======

N, M, L = map(int, input().split())
arr = [0]+list(map(int, input().split()))+[L]
arr.sort()

start, end = 1, L-1
result = 0
while start <= end:
    count = 0
    mid = (start+end) // 2
    for i in range(1, len(arr)):
        # 현재 거리 중 mid보다 큰 거리 찾기
        if arr[i]-arr[i-1] > mid:
            # 나눈 만큼 휴게소 설치 / 현재 설치 되어있는 구역 제외 -> -1
            count += (arr[i]-arr[i-1]-1) // mid
    if count > M:
        start = mid+1
    else:
        end = mid-1
        result = mid
print(result)

# - mid : 가장 멀리 떨어져 있는 휴게소 사이 거리
# - count : 설치해야 할 휴게소 개수
# - 모든 거리를 완전 탐색을 해서 mid보다 큰 경우, 해당 mid로 나누어서 설치해야 할 휴게소 개수를 구한다.
# - 설치해야 할 휴게소 개수가 M보다 크다면 mid는 더 길어야 한다.
# - 설치해야 할 휴게소 개수가 M보다 작다면 mid는 더 짧아야 한다. (조건 만족은 했으므로 result = mid)