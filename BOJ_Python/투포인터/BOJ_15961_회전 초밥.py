import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = []
for i in range(n):
    sushi.append(int(sys.stdin.readline()))

# 원형리스트 만들기
sushi.extend(sushi)

left, right = 0, 0
dic = defaultdict(int)
ans = 0

dic[c] += 1 # 보너스 초밥

# 1. k구간만큼 먹기
while right < k:
    dic[sushi[right]] += 1
    right += 1

# 2. 슬라이딩 윈도우
while right < len(sushi):
    ans = max(ans, len(dic))
    # 맨 왼쪽 초밥 제거
    dic[sushi[left]] -= 1
    if dic[sushi[left]] == 0:
        del dic[sushi[left]]
    # 오른쪽 초밥 추가
    dic[sushi[right]] += 1
    left += 1
    right += 1

print(ans)