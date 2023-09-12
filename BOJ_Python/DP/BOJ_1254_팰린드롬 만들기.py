# - 반복문을 통해 문자열의 문자를 확인한다.

# - i번째로 시작한 문자열과 i번째로 시작한 문자열을 뒤에서부터 확인한 문자열을 비교한다.

# - 두 문자열이 같을 경우 i번째 이전에 문자들을 문자열 뒤에 추가하면 팰린드롬을 만들 수 있다.

# - 현재 문자열의 개수와 i번째 이전에 문자의 개수를 더해서 출력한다.

import sys

s = sys.stdin.readline().rstrip()

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s) + i)
        break

