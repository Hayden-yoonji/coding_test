import itertools

def cnt_poss(k,dungeons):
    curr = k
    cnt = 0
    for d in dungeons:
        if curr >= d[0]:
            cnt += 1
            curr -= d[1]
        else: break
    return cnt

def solution(k, dungeons):
    poss = list(itertools.permutations(dungeons))
    answer = 0
    for p in poss:
        answer = max(answer, cnt_poss(k,p))
    return answer