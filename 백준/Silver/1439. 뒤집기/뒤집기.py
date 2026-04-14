target = input()

cnt = 0
for i in range(len(target)-1):
    if target[i] != target[i+1]:
        cnt +=1
print((cnt+1)//2)