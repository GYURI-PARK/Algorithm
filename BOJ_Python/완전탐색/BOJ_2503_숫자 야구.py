import sys
from itertools import permutations

n = int(sys.stdin.readline())
li = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    num, strike, ball = map(int, sys.stdin.readline().split())
    num = list(str(num))
    remove = 0

    for i in range(len(li)):
        strike_cnt = 0
        ball_cnt = 0

        i -= remove

        for j in range(3):
            num[j] = int(num[j])
            if num[j] in li[i]:
                if j == li[i].index(num[j]):
                    strike_cnt += 1
                else:
                    ball_cnt += 1

        if strike_cnt != strike or ball_cnt != ball:
            li.remove(li[i])
            remove += 1

print(len(li))