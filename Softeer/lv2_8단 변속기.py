import sys

num = []
num.append(list(map(int, sys.stdin.readline().split())))
ascending = False

if num[0][0] < num[0][1]:
    ascending = True

for i in range(1, 7):
    if num[0][i] < num[0][i+1] and ascending == True:
        ascending = True
    elif num[0][i] < num[0][i+1] and ascending == False:
        print('mixed')
        exit()
    elif num[0][i] > num[0][i+1] and ascending == False:
        ascending = False
    elif num[0][i] > num[0][i+1] and ascending == True:
        print('mixed')
        exit()

if ascending == True:
    print('ascending')
else:
    print('descending')
