def solution(want, number, discount):
    answer = 0
    dict = {i:j for i,j in zip(want,number)}
    slicing = len(discount)-9
    for k in range(slicing):
        dis_list = discount[k:k+10]
        dis_dict = {i:dis_list.count(i) for i in want}
        if dict == dis_dict:
            answer += 1
    return answer