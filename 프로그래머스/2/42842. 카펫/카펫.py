import math

def solution(brown, yellow):
    answer = []
    pair = []
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow%i == 0:
            pair.append((i,int(yellow//i)))
    for n1,n2 in pair:
        n1,n2 = max(n1,n2), min(n1,n2)
        brown_n = (n1+n2)*2+4
        if brown_n == brown:
            answer.append(n1+2)
            answer.append(n2+2)
    return answer