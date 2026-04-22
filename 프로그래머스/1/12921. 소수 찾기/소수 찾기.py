import math
def solution(n):
    answer = 0
    for i in range(2,n+1):
        for j in range(2, int(math.sqrt(i))+1): # n의 제곱근을 정수화 시켜준 후 + 1
            if i % j == 0:
                break
        else:
            answer += 1
    return answer