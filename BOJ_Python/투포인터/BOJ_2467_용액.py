import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(li) - 1

ans = abs(li[start] + li[end])
ans_left = start
ans_right = end

while start < end:
    tmp = li[start] + li[end]

    if abs(tmp) < ans:
        ans_left = start
        ans_right = end
        ans = abs(tmp)

        if abs(tmp) == 0:
            break
    
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(li[ans_left], li[ans_right])