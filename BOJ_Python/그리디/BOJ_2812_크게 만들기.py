# 앞에서부터 스택에 주어진 숫자를 하나씩 집어 넣으면서 
# 스택에 가장 최근에 들어온 값과 새로 들어온 값을 비교해서 스택에 들어있는 값이 더 작으면 pop

import sys
n, k = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline().rstrip())
res = []

for i in range(n):
    while k > 0 and res and res[-1] < num[i]:
        res.pop()
        k -= 1
    res.append(num[i])

# for문 이후에 k가 0이상일 경우
print(''.join(res[:len(res)-k]))

