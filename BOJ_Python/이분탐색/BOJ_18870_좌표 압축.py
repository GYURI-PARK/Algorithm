import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
res = list(set(li))
res.sort(key = lambda x:int(x))

def binarySearch(li, target, start, end):
    mid = (start + end) // 2
    if target == li[mid]:
        return mid
    elif target < li[mid]:
        return binarySearch(li, target, start, mid-1)
    else:
        return binarySearch(li, target, mid+1, end)
    
result = []
for i in li:
    start = 0
    end = len(res) - 1
    result.append(binarySearch(res, i, start, end))

for i in range(len(result)):
    print(result[i], sep=' ', end=' ')


# =====
# dictionary

n = int(sys.stdin.readline())
li_dic = {}
li = []
li.append(list(sys.stdin.readline().split()))
res = list(set(li[0]))
res.sort(key = lambda x: int(x))
for i in range(len(res)):
    li_dic[res[i]] = i
for i in li[0]:
    print(li_dic[i], sep=' ', end=' ')