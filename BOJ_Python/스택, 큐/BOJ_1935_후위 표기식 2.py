import sys

n = int(sys.stdin.readline())
input = sys.stdin.readline().rstrip()
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

res = []
tmp = ["+", "-", "*", "/"]

# A = 65
for i in input:
    if i not in tmp:
        res.append(num[ord(i)-65])
    else:
        second = res.pop()
        first = res.pop()

        if i == "+":
            res.append(first + second)
        elif i == "-":
            res.append(first - second)
        elif i == "*":
            res.append(first * second)
        else:
            res.append(round((first / second), 3))

print(format(res[0], ".2f"))