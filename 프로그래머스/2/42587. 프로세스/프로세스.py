from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i, pri in enumerate(priorities):
        queue.append((i,pri))
    
    while queue:
        i,pri = queue.popleft()
        
        if any(pri<q[1] for q in queue):
            queue.append((i,pri))
        else:
            answer += 1
            if location == i:
                return answer
