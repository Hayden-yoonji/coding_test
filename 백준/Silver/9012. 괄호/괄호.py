import sys

n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    order = sys.stdin.readline().strip()
    flag = True
    
    for par in order:
        if par == '(':
            stack.append(par)
            
        elif par == ')':
            if stack:
                stack.pop()
            else:
                flag = False
                break

    if flag and not stack:
        print('YES')
    else:
        print('NO')