import sys

ground = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
res = 1e6

# 가로 탐색
for i in range(3):
    sort_gr = sorted(ground[i])
    tmp = abs(sort_gr[0] - sort_gr[1]) + abs(sort_gr[1] - sort_gr[2])
    if tmp == 0:
        print(0)
        exit()
    else:
        res = min(res, tmp)

# 세로 탐색
for i in range(3):
    tmp = min(abs(ground[0][i] - ground[1][i]) + abs(ground[1][i] - ground[2][i]),
             abs(ground[0][i] - ground[2][i]) + abs(ground[1][i] - ground[2][i]),
             abs(ground[0][i] - ground[1][i]) + abs(ground[0][i] - ground[2][i]))
    if tmp == 0:
        print(0)
        exit()
    else:
        res = min(res, tmp)
print(res)