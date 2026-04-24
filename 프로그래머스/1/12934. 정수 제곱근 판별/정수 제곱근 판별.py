import math
def solution(n):
    answer = 0
    x = int(math.sqrt(n))
    if x**2 == n:
        answer = (x+1)**2
    else:
        answer = -1
    return answer