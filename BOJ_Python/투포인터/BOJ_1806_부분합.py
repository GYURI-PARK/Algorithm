# 합이 s이상이 되는 수열의 길이 중 가장 짧은 것

import sys

n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
sum = 0 # 합을 저장할 변수 
min_length = sys.maxsize

while True: 
    # 총 합이 s보다 클 경우, start를 하나씩 옮겨보면서 어디까지 길이가 줄어드나 확인
    if sum >= s:
        min_length = min(min_length, end-start)
        sum -= li[start]
        start += 1
    elif end == n:
        break
    # 만약 총합이 s를 넘지 못할 경우, right를 오른쪽으로 한칸씩 옮기며 s를 넘을때까지 더하기
    else:
        sum += li[end]
        end += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)