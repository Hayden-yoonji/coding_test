def solution(date1, date2):
    answer = 0
    for i in range(len(date1)):
        if date1[i] < date2[i]:
            answer =1
            return answer
        elif date1[i] > date2[i]:
            answer = 0
            return answer
    return answer