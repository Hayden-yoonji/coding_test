def solution(sequence, k):
    s = 0
    e = 0
    interval = 0
    
    min_len = float('inf')
    for s in range(len(sequence)):
        while interval < k and e < len(sequence):
            interval += sequence[e]
            e += 1
        if interval == k:
            curr_len = (e-1)-s
            
            if curr_len < min_len:
                min_len = curr_len
                answer=[s,e-1]
        interval -= sequence[s]
    print(answer)
    return answer