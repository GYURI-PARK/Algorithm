# 결과값을 각 스태프들이 풍선을 만드는데 걸리는 시간으로 나눈 몫의 합이 풍선 개수
# 나올수 있는 최대 시간 = 7*8
# 몫의 합이 m보다 클 경우 => 시간 범위가 작아져야됨
# 몫의 합이 M보다 작을 경우 => 커져야됨

n, m = map(int, input().split())
li = list(map(int, input().split()))
start, end = 0, max(li) * m
res = 0
while start <= end:
    mid = (start + end)//2
    if sum([mid // n for n in li]) >= m:
        res = mid
        end = mid - 1
    else:
        start = mid +1
print(res)