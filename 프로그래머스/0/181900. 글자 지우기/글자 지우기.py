def solution(my_string, indices):
    answer = ''
    my_list = list(my_string)
    for i in indices:
        my_list[i] = ''
    answer = ''.join(my_list)
    return answer