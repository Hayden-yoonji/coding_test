def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            if i == 0:
                answer += a
            else:
                answer += a + d*i
    return answer