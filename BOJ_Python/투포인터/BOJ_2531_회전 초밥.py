import sys

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = []
for i in range(n):
    sushi.append(int(sys.stdin.readline()))

left, right = 0, k-1
ans = set()

while left < n:
    if right >= n:
        # 원형 연결 리스트
        right -= n
    if right < left:
        plates = sushi[left:] + sushi[:right+1]
    else:
        plates = sushi[left:right+1]
    
    cases = set(plates)

    if c not in cases:
        cases.add(c)
    if len(ans) < len(cases):
        ans = cases
    left += 1
    right += 1

print(len(ans))
