import sys
sys.setrecursionlimit(10 ** 9)

arr = []

while True:
    try: 
        arr.append(int(sys.stdin.readline().rstrip()))
    except:
        break

def preorder(start, end):
    if start > end:
        return

    mid = end + 1

    for i in range(start + 1, end + 1):
        if arr[start] < arr[i]:
            mid = i
            break

    # 왼쪽 서브트리
    preorder(start+1, mid-1)

    # 오른쪽 서브트리
    preorder(mid, end)

    # 출력
    print(arr[start])
preorder(0, len(arr)-1)