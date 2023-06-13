# sen = "."이 될 때까지
# stack = 빈 배열 생성 sen를 돌면서 ( 또는 [ 를 만나면 stack에 추가
# ) 또는 ]를 만나면 
# stack.pop()이 )또는 ]와 같으면 (stack pop()) 한번더?
# stack이 비어있다면 print("yes") 아니면 print("no")

# ❗️
# readline()으로 입력받을 때 rstrip()으로 개행문자 제거 해주기

import sys

while True:
    stack = []
    sen = sys.stdin.readline().rstrip()
    if sen == ".":
        break

    for i in sen :
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" :
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break

        elif i == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")