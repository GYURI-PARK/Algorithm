import sys

n, m = map(int, sys.stdin.readline().split())
li = [sys.stdin.readline().rstrip() for _ in range(n)]
ans = 0

for i in range(m):
    test = sys.stdin.readline().rstrip()
    for j in li:
        if test == j[:len(test)]:
            ans += 1
            break
print(ans)