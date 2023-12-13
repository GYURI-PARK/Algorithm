import sys

trees = dict()
cnt = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    cnt += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    
sorts = dict(sorted(trees.items()))
for i in sorts:
    per = (sorts[i] / cnt * 100)
    print("%s %.4f" %(i, per))
