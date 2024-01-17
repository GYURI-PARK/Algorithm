import sys

n, m = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]

start, end = min(li), sum(li)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    tmp = mid # 현재 인출한 돈

    for i in range(n):
        if tmp < li[i]:
            cnt += 1 
            tmp = mid # 남은 돈 넣고, 다시 뽑음
        tmp -= li[i]

    # 인출 금액이 적을 경우 = 인출 횟수가 m보다 많음
    if cnt > m or mid < max(li):
        start = mid + 1
    # 인출 금액이 같거나 큼 = 인출 횟수가 m보다 적거나 같음
    else:
        end = mid - 1
        res = mid
print(res)