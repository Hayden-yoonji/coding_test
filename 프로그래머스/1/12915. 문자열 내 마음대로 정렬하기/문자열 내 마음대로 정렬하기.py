def solution(strings, n):
        
    answer = []
    keys = [(word[n], word) for word in strings]
    sorted_keys = sorted(keys)
    for w in sorted_keys:
        answer.append(w[1])
    return answer