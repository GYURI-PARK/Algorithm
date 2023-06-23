# 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
# 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

# 입력받는 건 순위 !!! 낮을수록 좋음 !!!

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    scores = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        scores.append((a, b))

    scores.sort()

    min_interview_score = scores[0][1]
    count = 1

    for i in range(1, n):
        if scores[i][1] <= min_interview_score:
            min_interview_score = scores[i][1]
            count += 1

    print(count)