def solution(s):
    
    stack = []
    if s[0] != '(':
        return False
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                stack.pop()
                
    return not(len(stack))

