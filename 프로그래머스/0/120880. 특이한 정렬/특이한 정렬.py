def solution(numlist, n):
    answer = []
    tmp = []
    for number in numlist:
        distance = abs(number - n)
        tmp.append((distance,number*(-1)))
    sorted_tmp = sorted(tmp)
    for i in range(len(sorted_tmp)):
        answer.append(sorted_tmp[i][1] * (-1))
    return answer