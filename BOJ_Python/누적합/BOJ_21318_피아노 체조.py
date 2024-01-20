import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())

mistake = [0 for _ in range(n)]
for i in range(1, n):
    if li[i] < li[i-1]:
        mistake[i] = mistake[i-1] + 1
    else:
        mistake[i] = mistake[i-1]
# print(mistake)


for i in range(q):
    x, y = map(int, sys.stdin.readline().split())
    print(mistake[y-1] - mistake[x-1])
    # 각 자리마다 실수 몇번 해놨는지 더해놓고 y-x
