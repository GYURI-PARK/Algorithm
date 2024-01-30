import sys
from collections import deque

t = int(sys.stdin.readline())

li = [[1,1,1,0,1,1,1],
     [0,0,1,0,0,1,0],
     [0,1,1,1,1,0,1],
      [0,1,1,1,0,1,1],
     [1,0,1,1,0,1,0],
     [1,1,0,1,0,1,1],
     [1,1,0,1,1,1,1],
     [1,1,1,0,0,1,0],
     [1,1,1,1,1,1,1],
     [1,1,1,1,0,1,1]]

for _ in range(t):
    a, b = map(str, sys.stdin.readline().split())
    deq_a = deque(a)
    deq_b = deque(b)
    res = 0
    
    while True:
        if len(deq_a) < 1 or len(deq_b) < 1:
            break
    
        first = deq_a.pop()
        second = deq_b.pop()
        first_li = li[int(first)]
        second_li = li[int(second)]
        
        for k in range(7):
            if first_li[k] + second_li[k] == 1:
                res += 1
            


    if len(deq_a) != 0:
        while len(deq_a) > 0:
            tmp = deq_a.pop()
            for i in range(7):
                res += li[int(tmp)][i]
            
    else:
        while len(deq_b) > 0:
            tmp = deq_b.pop()
            for i in range(7):
                res += li[int(tmp)][i]
    print(res)
    

# ============== 참고 ==============

info = {
    
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010', 
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    ' ' : '0000000'
}


t = int(input())
for _ in range(t):
    a, b = map(str,input().split())
    
    
    # 0을 처리하는 과정
    a_zero, b_zero = 5-len(a), 5-len(b)
    a = ' ' * a_zero + a
    b = ' ' * b_zero + b

    result = 0

    for i in range(5):
        for j in range(7):
            if(info[a[i]][j] != info[b[i]][j]):
                result+=1
                
    print(result)