import sys

r, c, n = map(int, sys.stdin.readline().split())
graph = []


for i in range(r):
    graph.append(list(sys.stdin.readline().strip()))

# n이 짝수일 경우에는 항상 모든 곳에 폭탄 설치
# n이 1일 때는 초기상태와 동일
# (n이 1일 경우 제외) n%4 == 1: 초기상태에서 폭탄이 2번 터진 경우
# n%4 == 3: 초기상태에서 폭탄이 1번 터진 경우

def bomb(graph):
    res = [['O' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '0':
                res[i][j] = '.'
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < r and 0 <= y < c:
                        res[x][y] = '.'
    return res

if n == 1:
    for i in range(r):
        print(''.join(graph[i]))
elif n % 2 == 0:
    for i in range(r):
        print('0' * c)
elif n % 4 == 3:
    res = bomb(graph)
    for i in range(r):
        print(''.join(res[i]))
elif n % 4 == 1:
    res = bomb(graph)
    res = bomb(res)
    for i in range(r):
        print(''.join(res[i]))
