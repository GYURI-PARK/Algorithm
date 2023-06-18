n = int(input())
li = list(map(int, input().split()))
m = int(input())

start, end = 0, max(li)
while start <= end:
    mid = (start + end) // 2
    sum = 0 # 예산 총액
    for i in li:
        if i >= mid: # 요청한 금액이 상한액 이상
            sum += mid # 상한액 더하기
        else:
            sum += i 
    if sum <= m: # 예산 총액이 총 예산 이하
        start = mid + 1
    else:
        end = mid - 1
    
print(end)
