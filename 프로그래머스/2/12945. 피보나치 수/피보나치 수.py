def solution(n):
    pre,cur = 0,1
    for i in range(2,n+1):
        pre,cur = cur, pre+cur
    return cur %1234567
    
    