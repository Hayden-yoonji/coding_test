from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    all_words = []
    
    # 1. 1글자부터 5글자까지의 모든 조합을 만듭니다.
    for i in range(1, 6):
        for p in product(vowels, repeat=i):
            # 튜플을 문자열로 합쳐서 리스트에 넣습니다.
            all_words.append(''.join(p))
            
    # 2. 사전순으로 정렬합니다.
    all_words.sort()
    
    # 3. 인덱스에 1을 더해 반환합니다.
    return all_words.index(word) + 1