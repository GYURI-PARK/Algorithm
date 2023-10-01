# https://school.programmers.co.kr/learn/courses/30/lessons/64065# 

def solution(s):
    splits = s[2:-2]
    strings = splits.split('},{')
    strings.sort(key = len)
    answer = []
    for i in strings:
        ii = i.split(',')
        for j in range(len(ii)):
            if int(ii[j]) not in answer:
                answer.append(int(ii[j]))
    return answer
