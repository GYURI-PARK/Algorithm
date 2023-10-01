# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# 소수 판별 함수
# 소수 -> true
def sosu(n):
    a = 0
    if n < 2: 
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                a = 1
                break
    if a == 0:
        return True
    else:
        return False
                

def solution(n, k):
    res = ""
    
    while n > 0:
        n, mod = divmod(n, k)
        res += str(mod)
    res = res[::-1]
        
    string = res.split('0')
    answer = 0
    for i in string:
        if len(i) > 0 and sosu(int(i)):
            answer += 1
    
    return answer

# 소수 판별 함수에서 범위를 for i in range(2, int(n**0.5)+1): 이렇게 하지 않고,
# n까지로 두면 시간초과 남 !!