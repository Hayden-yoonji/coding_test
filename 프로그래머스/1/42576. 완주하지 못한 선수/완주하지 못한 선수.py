def solution(participant, completion):
    answer = ''
    hash_dict = {}
    for p in participant:
        if p in hash_dict:
            hash_dict[p] += 1
        else:
            hash_dict[p] =1
    
    for c in completion:
        hash_dict[c] -= 1
        
    for key in hash_dict:
        if hash_dict[key] >0:
            answer += key
    return answer
