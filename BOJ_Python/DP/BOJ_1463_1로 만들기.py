n = int(input())

d = [0] * (n+1) # 1-based
# d[i] = i를 1로 만들기 위해 필요한 연산 사용횟수의 최솟값
# d[k] -> 1. 3으로 나눠지면 3으로 나눔 (d[k] = d[k/3] + 1)
# 2. 2로 나눠지면 2로 나눔 (d[k] = d[k/2] + 1)
# 3. 1을 빼거나 (d[k] = d[k-1] + 1)
# 이들 중에서 최솟값

for i in range(2, n+1): 
    d[i] = d[i-1] + 1 # 1을 빼는 연산 -> 1회 진행
    if i % 2 == 0: 
        d[i] = min(d[i], d[i//2] + 1)
    if i%3==0: 
        d[i] = min(d[i], d[i//3] + 1)
print(d[n])