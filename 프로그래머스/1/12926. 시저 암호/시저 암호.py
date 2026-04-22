def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        else:
            base = ord('A') if i.isupper() else ord('a')
            answer += chr((ord(i) - base + n)%26 + base)
        
    return answer