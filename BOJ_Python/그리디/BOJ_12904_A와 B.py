import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

while len(s) < len(t):
    if t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    else:
        t = t[:-1]

if s == t:
    print(1)
else:
    print(0)
