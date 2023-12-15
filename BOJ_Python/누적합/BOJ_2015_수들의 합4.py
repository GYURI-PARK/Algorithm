# 누적합 문제
# 1. 
import sys

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

sum_dict = {0: 1}

sum = 0
answer = 0

for i in li:
    sum += i

    if sum - k in sum_dict.keys():
        answer += sum_dict[sum - k]

    sum_dict[sum] = sum_dict.get(sum, 0) + 1

print(answer)

# 2. 

import sys

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

sum = [0] # 누적합을 저장할 리스트

for i in range(0, n):
    sum.append(sum[-1] + li[i])


## 음수가 존재하고 k의 값이 큰 값일 경우에는 딕셔너리 사용
cnt = {} # 값의 개수를 저장할 딕셔너리
ans = 0

for i in range(n+1):
    ans += cnt.get(sum[i]-k, 0)
    cnt[sum[i]] = cnt.get(sum[i], 0) + 1

print(ans)

## cf) 모든 값들이 양수이고(누적합이 계속해서 증가) k의 값이 적당할 경우에는 아래와 같이 리스트 사용
# cnt = [0 for _ in range(10010)]
# ans = 0
# for i in range(1, n+1):
#   ans += cnt[sum[i]-k]
#   cnt[sum[i]] += 1
# print(ans)
