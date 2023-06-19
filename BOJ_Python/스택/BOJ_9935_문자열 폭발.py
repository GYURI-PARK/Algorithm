# stack에 sen 하나씩 추가하면서 stack[-len(bomb): ] == bomb이면 
# len(bomb)민큼 pop해주기
# 💡 '구분자'.join(리스트) = 구분자로 문자열 합치기

import sys

sen = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []

for i in range(len(sen)):
    stack.append(sen[i])
    if ''.join(stack[-len(bomb):]) == bomb:
        for j in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack[:]))


