import sys

sudoku = []
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().rstrip())))

# 0인 좌표 저장
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i,j))

# 행 검사
def row_check(r, num):
    for x in range(9):
        if num == sudoku[r][x]:
            return False
    return True

# 열 검사
def col_check(c, num):
    
    for x in range(9):
        if num == sudoku[x][c]:
            return False
    return True


# 3x3 검사
def three_check(r, c, num):
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if r != nr + x and nc + y and sudoku[nr+x][nc+y] == num:
                return False
    return True

def dfs(depth):
    # 0의 개수에 도달
    if depth >= len(zeros):
        for k in range(9):
            print(''.join(map(str, sudoku[k])))
        exit()
    nr, nc = zeros[depth]
    
    for j in range(1, 10):
        # 조건에 맞는 것만 dfs를 돈다.
        if row_check(nr, j) and col_check(nc, j) and three_check(nr, nc, j):
            sudoku[nr][nc] = j
            dfs(depth + 1)
            sudoku[nr][nc] = 0

dfs(0)