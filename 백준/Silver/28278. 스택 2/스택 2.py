import sys
stack = []

n = int(sys.stdin.readline())

for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == '1':
        stack.append(order[1])
    elif order[0] == '2':
        if stack:
            print(stack.pop())
            continue
        print(-1)
    elif order[0] == '3':
        print(len(stack))
    elif order[0] == '4':
        if stack:
            print(0)
            continue
        print(1)
    elif order[0] == '5':
        if stack:
            print(stack[-1])
            continue
        print(-1)
        