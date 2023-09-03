import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(li) - 1
ans = 0

# ❗️ 처음과 맨 마지막에서 시작해 포인터를 옮길 때 사이에 존재하는 개발자 수는 항상 줄어듦 ❗️
# ❗️ 따라서 start와 end 중 더 작은 값을 이동시킬 때 더 큰 능력치를 얻을 수 있음 ❗️
while start + 1 < end:
    ans = max(ans, ((end-start-1) * min(li[start], li[end])))
    if li[start] < li[end]:
        start += 1
    else:
        end -= 1
print(ans)