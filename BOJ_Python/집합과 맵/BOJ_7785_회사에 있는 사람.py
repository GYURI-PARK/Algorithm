import sys

n = int(sys.stdin.readline())
res = dict()

for i in range(n):
    input = list(sys.stdin.readline().split())
    if input[1] == "enter":
        res[input[0]] = input[1]
    else:
        del res[input[0]]

res = sorted(res.keys(), reverse=True)

for i in res:
    print(i)