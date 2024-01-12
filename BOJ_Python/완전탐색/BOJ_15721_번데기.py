import sys

a = int(sys.stdin.readline())
t = int(sys.stdin.readline())
num = int(sys.stdin.readline())

bun, degi = 0, 0
turn = 0 # 몇 바퀴 돌았는지
li = []

while True:
    turn += 1

    # 번-데기-번-데기
    for _ in range(2):
        bun += 1
        degi += 1
        li.append((0, bun))
        li.append((1, degi))
    for _ in range(turn + 1):
        bun += 1
        li.append((0, bun))
    for _ in range(turn + 1):
        degi += 1
        li.append((1, degi))

    if bun >= t:
        print(li.index((num, t)) % a)
        break