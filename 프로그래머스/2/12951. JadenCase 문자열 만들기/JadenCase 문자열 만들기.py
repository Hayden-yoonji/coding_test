def solution(s):

    word = s.split(' ')
    result = []

    for w in word:
        if w[:1].isalpha():
                new_word = w[:1].upper() + w[1:].lower()  
        else:
            new_word = w[:1] + w[1:].lower()  
        result.append(new_word)  

    return " ".join(result)