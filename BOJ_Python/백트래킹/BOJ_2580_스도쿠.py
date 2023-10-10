# 83%에서 시간초과 계속뜸

import sys

sudoku = []
zeros = []

for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i,j))

# 열 체크
def check_col(col, num):
    for x in range(9):
        if num == sudoku[x][col]:
            return False
    return True
        
# 행 체크
def check_row(row, num):
    for x in range(9):
        if num == sudoku[row][x]:
            return False
    return True

# 3 * 3 체크
def three_check(r, c, num):
    for x in range(3):
        for y in range(3):
            if num == sudoku[r//3*3+x][c//3*3+y]:
                return False
    return True

def backtracking(depth):
    if depth == len(zeros):
        for i in sudoku:
            print(*i)
        exit()
    nr, nc = zeros[depth]
    
    for j in range(1, 10):
        if check_row(nr,j) and check_col(nc, j) and three_check(nr, nc, j):
            sudoku[nr][nc] = j
            backtracking(depth+1)
            sudoku[nr][nc] = 0
backtracking(0)