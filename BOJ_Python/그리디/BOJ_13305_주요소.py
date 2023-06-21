# 첫번째 주유소부터 시작해서 값이 더 싸면 교체
import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
# res = []

res = distance[0] * price[0]
# 가장 싼곳
cheapest = price[0]

for i in range(1, n-1):
    if cheapest > price[i]:
        cheapest = price[i]

    res += cheapest * distance[i]
print(res)