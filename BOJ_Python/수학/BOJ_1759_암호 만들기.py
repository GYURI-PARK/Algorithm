import sys

l, c = map(int, sys.stdin.readline().split())
li = list(sys.stdin.readline().split())
li.sort()

moeum = ["a", "e", "i", "o", "u"]
res = []

def backtracking(depth):
    if len(res) == l:
        mo, ja = 0, 0

        for i in range(l):
            if res[i] in moeum:
                mo += 1
            else:
                ja += 1

        if mo >= 1 and ja >= 2:
            print(''.join(map(str, res)))
        return

    for i in range(depth, c):
        if li[i] in res:
            continue
        res.append(li[i])  
        backtracking(i)
        res.pop()

backtracking(0)
