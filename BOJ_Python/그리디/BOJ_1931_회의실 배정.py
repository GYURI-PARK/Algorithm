import sys

n = int(sys.stdin.readline())
li = []
res = 1


for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
    
sortedList = sorted(li, key = lambda x: (x[1], x[0]))
# 첫번째 값 담아놓기
# 두번째부터 앞의 end값 보다 뒤의 start가 클경우 tmp를 뒤의 end값으로 갱신

endTime = sortedList[0][1]

for i in range(1, n):
    if sortedList[i][0] >= endTime:
        endTime = sortedList[i][1] 
        res += 1

print(res)


# 정렬 필요
# start기준으로 하면 모든 경우의 수 판별 못함
