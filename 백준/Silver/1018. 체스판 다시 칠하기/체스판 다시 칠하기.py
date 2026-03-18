n,m = map(int,input().split())
info = []
cnt = []
for _ in range(n):
    info.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        start_w = 0
        start_b = 0
        for a in range(i, i+8):
            for b in range(j, j+8):     
                if (a+b)%2 == 0:
                    if info[a][b] != 'B':   #흰색으로 시작
                        start_b +=1
                    if info[a][b] != 'W':   #검은색으로 시작 -> 
                        start_w +=1
                else:
                    if info[a][b] != 'B':
                        start_w += 1
                    if info[a][b] != 'W':
                        start_b += 1
        cnt.append(min(start_w, start_b))
print(min(cnt))