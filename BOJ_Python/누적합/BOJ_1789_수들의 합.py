# 최대한 많은 자연수를 사용해 S를 만들기 위해선 서로 다른 자연수들이 최소가 되어야한다.
import sys

n = int(sys.stdin.readline())

total = 0
cnt = 0

while True:
    cnt += 1
    total += cnt
    if total > n:
        break

print(cnt-1)