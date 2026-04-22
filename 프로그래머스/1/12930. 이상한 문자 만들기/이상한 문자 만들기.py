def solution(s):
    answer = []
    words = s.split(' ')
    
    for n in words:
        new_word = ''
        for i in range(len(n)):
            if i%2== 0:
                new_word += n[i].upper()
            else:
                new_word += n[i].lower()      
        answer.append(new_word)
    return ' '.join(answer)