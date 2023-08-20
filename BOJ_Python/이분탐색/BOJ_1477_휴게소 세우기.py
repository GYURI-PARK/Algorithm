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
        if arr[i]-arr[i-1] > mid:
            count += (arr[i]-arr[i-1]-1)//mid
    if count > M:
        start = mid+1
    else:
        end = mid-1
        result = mid
print(result)