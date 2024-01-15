import sys

keyboard = [['q','w','e','r','t','y','u','i','o','p'],
            ['a','s','d','f','g','h','j','k','l'],
            ['z','x','c','v','b','n','m']]

sl, sr = sys.stdin.readline().split()
for i in range(3):
    for j in range(len(keyboard[i])):
        if sl == keyboard[i][j]:
            # 자음
            x1, y1 = i, j
        elif sr == keyboard[i][j]:
            # 모음
            x2, y2 = i, j

string = sys.stdin.readline().rstrip()
res = 0

for i in range(len(string)):
    for list in range(3):
        if string[i] in keyboard[list]:
            idx1 = list
            for j in range(len(keyboard[list])):
                if string[i] == keyboard[list][j]:
                    idx2 = j
    if (idx1 != 2 and idx2 < 5) or (idx1 == 2 and idx2 < 4):
        # 왼손 이용할 경우
        res += abs(idx1-x1) + abs(idx2-y1)
        x1, y1 = idx1, idx2
    else:
        # 오른손 이용할 경우
        res += abs(idx1-x2) + abs(idx2-y2)
        x2, y2 = idx1, idx2

res += len(string)
print(res)