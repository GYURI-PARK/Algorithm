import sys

n = int(sys.stdin.readline())
num = int(sys.stdin.readline())

graph = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = n // 2
y = n // 2

tmp = 1  # 해당 위치에 들어갈 숫자
graph[x][y] = tmp
length = 0 # 특정 방향으로 이동할 길이 증가 정도

ans = []

while True:
    for i in range(4):
        for _ in range(length):
            x += dx[i]
            y += dy[i]
            tmp += 1
            graph[x][y] = tmp

            if tmp == num:
                ans = [x+1, y+1]
    
    if x == y == 0:
        break

    x -= 1
    y -= 1
    length += 2

for i in range(n):
    print(*graph[i])

if num == 1:
    print(n//2+1, n//2+1)
else:
    print(*ans) 


