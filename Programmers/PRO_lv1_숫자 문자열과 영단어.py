# dictionary 사용하지말고 인덱스로 접근하기

def solution(s):
    res = ''
    tmp = ''
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for j in s:
        if(j.isnumeric()):
            res += j
        else:
            tmp += j
            if tmp in arr:
                res += str(arr.index(tmp))
                tmp = ''
    return int(res)


# 딕셔너리 이용한 풀이

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)