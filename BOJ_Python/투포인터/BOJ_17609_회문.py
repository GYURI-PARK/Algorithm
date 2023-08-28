# import sys

# t = int(sys.stdin.readline())

# for i in range(t):
#     s = list(sys.stdin.readline().rstrip())
#     tmp = []
#     for j in range(len(s)):
#         if s[j] not in tmp:
#             tmp.append(s[j])
#         elif s[j] == tmp[len(tmp)-1]:
#             tmp.pop()
#         elif s[j] in tmp and tmp[0] == s[j]:
#             tmp.remove(s[j])

#     print('tmp', tmp)
#     if len(tmp) == 0 :
#         print(0)
#     elif len(tmp) == 1:
#         print(1)
#     else:
#         print(2)

import sys

t = int(sys.stdin.readline())

# 유사회문 여부 판단 함수
def isPseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# 회문 여부 판단 함수
def isPalindrome(word, left, right):
    if word == word[::-1]:
        return 0
    else:
        while left < right:
            if word[left] != word[right]:
                check_left = isPseudo(word, left + 1, right)
                check_right = isPseudo(word, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

for i in range(t):
    s = list(sys.stdin.readline().rstrip())
    left, right = 0, len(s)-1
    ans = isPalindrome(s, left, right)
    print(ans)


