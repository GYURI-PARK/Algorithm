import sys
n, k, q, m = map(int, sys.stdin.readline().split())

sleeping = [False for _ in range(n+3)]

for i in map(int, sys.stdin.readline().split()):
    sleeping[i] = True

check = [1 for _ in range(n+3)]

for i in map(int, sys.stdin.readline().split()):
    if sleeping[i]:
        continue

    for j in range(i, n+3, i):
        if sleeping[j]:
            continue
        check[j] = 0
        
tmp = 0
check[2] = 0

for i in range(3, n+3):
    if check[i]:
        tmp += 1
    check[i] = tmp

for _ in range(m):
    s,e = map(int, sys.stdin.readline().split())
    print(check[e]-check[s-1])

# ==================================================================