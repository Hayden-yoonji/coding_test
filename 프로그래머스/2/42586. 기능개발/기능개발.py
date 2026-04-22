import math

def solution(progresses, speeds):
    answer = []
    stack = []
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i])/speeds[i])
        if stack and max(stack) < days:
            answer.append(len(stack))
            stack.clear()
            stack.append(days)
        else:
            stack.append(days)
    if stack:
        answer.append(len(stack))
    
    return answer