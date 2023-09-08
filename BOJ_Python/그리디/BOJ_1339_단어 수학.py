import sys

n = int(sys.stdin.readline())
alpha_dict = {'A':0, 'B': 0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alpha_list = []
value_list = []

for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    alpha_list.append(tmp)
    for j in range(len(tmp)):
        # j : 0부터 len(tmp)-1까지
        val = 10 ** (len(tmp)-j-1)
        alpha_dict[tmp[j]] += val
    
# dict에서 val값이 큰 순서대로 나열

for i in alpha_dict.values():
    if i > 0:
        value_list.append(i)

value_list.sort(reverse=True)

ans = 0
num = 9
for i in range(len(value_list)):
    tmp = num * value_list[i]
    ans += tmp
    num -= 1

print(ans)

# 알파벳마다 각 자리수를 구한다
# AAA -> 111
# GCF -> G: 100, C:10, F:1
# 큰 순서대로 9,8,7, ...를 할당