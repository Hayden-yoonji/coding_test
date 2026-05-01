from collections import defaultdict

def solution(clothes):
    answer = 1
    category = defaultdict()
    for cloth, kind in clothes:
        category[kind] = category.get(kind,0) +1
    for cnt in category.values():
        answer *= (cnt+1)
    return answer-1