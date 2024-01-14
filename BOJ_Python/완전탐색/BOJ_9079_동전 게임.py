import sys
from collections import deque

t = int(sys.stdin.readline())

def flip(numbers, arr):
    for num in numbers:
        arr[num] = '0' if arr[num] == '1' else '1'
    return arr

def sol(arr):

    cases = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    visited = [False] * 512
    visited[int(''.join(arr), 2)] = True

    q = deque([(int(''.join(arr), 2), 0)])
    while q:
        tmp, count = q.popleft()

        if tmp == 0 or tmp == 511:
            return count
        for numbers in cases:
            newArr = flip(numbers, list(bin(tmp)[2:].zfill(9)))
            vs = int(''.join(newArr), 2)
            if not visited[vs]:
                visited[vs] = True
                q.append((int(''.join(newArr), 2), count + 1))
    return -1

for i in range(t):
    graph = list(list(sys.stdin.readline().split()) for _ in range(3))
    graph = ['1' if graph[y][x] == 'H' else '0' for y in range(3) for x in range(3)]
    print(sol(graph))