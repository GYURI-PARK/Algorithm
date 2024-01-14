import sys

h, w = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

res = 0

for i in range(n):
    for j in range(i+1, n):
        h1, w1 = sticker[i][0], sticker[i][1]
        h2, w2 = sticker[j][0], sticker[j][1]
        
        if (h1+h2 <= h and max(w1, w2) <= w) or (max(h1, h2) <= h and w1+w2 <= w):
            res = max(res, h1*w1 + h2*w2)
        if (h1+w2 <= h and max(h2, w1) <= w) or (max(h1, w2) <= h and h2+w1 <= w):
            res = max(res, h1*w1 + h2*w2)
        if (w1+h2 <= h and max(w2, h1) <= w) or (max(w1, h2) <= h and w2+h1 <= w):
            res = max(res, h1*w1 + h2*w2)
        if (w1+w2 <= h and max(h1, h2) <= w) or (max(w1, w2) <= h and h1+h2 <= w):
            res = max(res, h1*w1 + h2*w2)
print(res)