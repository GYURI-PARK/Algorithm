import sys
n, m = map(int, sys.stdin.readline().split())
t = []
for i in range(n):
    t.append(int(sys.stdin.readline()))

start = min(t)
end = max(t) * m
res = end

while start <= end:
    total = 0
    # mid시간 동안 검사할 수 있는 총 사람 수
    mid = (start + end) // 2
    for i in range(n):
        total += mid // t[i]
       
    if total >= m:
        end = mid - 1
        res = min(res, mid)
    else:
        start = mid + 1

print(res)