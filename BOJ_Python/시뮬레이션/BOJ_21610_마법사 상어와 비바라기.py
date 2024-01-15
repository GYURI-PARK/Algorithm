import sys

n, m = map(int, sys.stdin.readline().split())
# A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양
# i번째 이동 명령은 방향 di과 거리 si

A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
direction = [(0,-1), (-1, -1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
# 구름 좌표
cloud = [[n-1,0], [n-1,1], [n-2,0], [n-2,1]]
order = []

for i in range(m):
    order.append(list(map(int, sys.stdin.readline().split())))

for d, s in order:
    for i in range(len(cloud)):
        dx = cloud[i][0] + (s * direction[d-1][0])
        dy = cloud[i][1] + (s * direction[d-1][1])

        dx %= n
        dy %= n

        A[dx][dy] += 1
        cloud[i] = [dx, dy]

    for x, y in cloud:
        # 물복사 버그
        for dir in range(1, 8, 2):
            nx = x + direction[dir][0]
            ny = y + direction[dir][1]

            if 0 <= nx < n and 0 <= ny < n:
                if A[nx][ny] != 0:
                    A[x][y] += 1
        
        A[x][y] *= -1

    cloud.clear()

    for i in range(n):
        for j in range(n):
            if A[i][j] >= 2:
                cloud.append([i,j])
                A[i][j] -= 2
            elif A[i][j] < 0:
                A[i][j] *= -1

res = 0
for i in range(n):
    for j in range(n):
        res += A[i][j]

print(res)