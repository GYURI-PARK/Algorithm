import sys

n = int(sys.stdin.readline())

# 팰린드롬 판단
def isPalindrome(sen, start, end):
    if sen == sen[::-1]:
        return 0
    else:
        while start < end:
            if sen[start] != sen[end]:
                check_left = isPseudo(sen, start + 1, end)
                check_right = isPseudo(sen, start, end-1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                start += 1
                end -= 1


# 유사회문 판단
def isPseudo(sen, start, end):
    while start < end:
        if sen[start] == sen[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


for i in range(n):
    sen = sys.stdin.readline().rstrip()
    print(isPalindrome(sen, 0, len(sen)-1))
