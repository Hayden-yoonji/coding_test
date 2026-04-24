def solution(s):
    answer = ''
    new = list(s)
    ascii = []
    for i in new:
        ascii.append(ord(i))
    ascii.sort(reverse=True)
    for j in ascii:
        answer += chr(j)
    return answer