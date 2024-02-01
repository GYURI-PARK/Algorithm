import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
room = dict()
for _ in range(n):
    room[sys.stdin.readline().rstrip()] = []
for _ in range(m):
    name, start, end = sys.stdin.readline().split()
    room[name].append([int(start), int(end)])

# room의 각 리스트를 start를 기준으로 오름차순 정렬
for key in room.keys():
    room[key] = sorted(room[key], key=lambda x: x[0])

sort_dict = dict(sorted(room.items()))
idx = 0
for i in sort_dict.keys():
    print('Room', i+':')
    res = []
    que = deque((18, 9))
    for j in range(len(sort_dict[i])):
        if len(que) > 0:
            a = que.pop()
            if a < sort_dict[i][j][0]:
                res.append([a, sort_dict[i][j][0]])
                que.append(sort_dict[i][j][1])
            else:
                que.append(sort_dict[i][j][1])
    for k in range(len(que)):
        a = que.pop()
        if a < 18:
            res.append([a, 18])
    # print('res', res)
    if len(res) == 0:
        print('Not available')
    else:
        print(len(res), 'available')
        for r in res:
            print(str(r[0]).zfill(2)+'-'+str(r[1]))
    idx += 1
    if idx < len(sort_dict):
        print('-----')
            
        
    