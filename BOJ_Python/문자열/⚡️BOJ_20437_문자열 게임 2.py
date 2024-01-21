import sys
from collections import defaultdict

t = int(sys.stdin.readline())

def length(dic):
    min_length = 10000
    max_length = 0

    for i in dic:
        for j in range(len(dic[i]) - k + 1):
            length = dic[i][j+k-1] - dic[i][j] + 1
            min_length = min(min_length, length)
            max_length = max(max_length, length)
    return(min_length, max_length)

for _ in range(t):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())

    dic = defaultdict(list)
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            dic[w[i]].append(i)
    if not dic:
        print(-1)
    else:
        print(*length(dic))