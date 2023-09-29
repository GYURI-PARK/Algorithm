import sys

n = int(sys.stdin.readline())

row = [0] * n
res = 0

# 맨 윗줄 첫번째 칸부터 한줄씩 내려오면서 가능한 칸 확인
# 가능한 칸이 없으면 다시 위로 올라가서 다음 칸 확인

def adjacent(x):
    for i in range(x):
        # 열이 같거나 대각선에 있으면 False 반환
        # 행 - 행 = 열 - 열 : 대각선
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False  
    return True
        

def dfs(x):
    global res

    if x == n:
        res += 1
    # 각행에 퀸 놓기
    else:
        for i in range(n):
            row[x] = i
            if adjacent(x):
                dfs(x+1)

dfs(0)
print(res)
