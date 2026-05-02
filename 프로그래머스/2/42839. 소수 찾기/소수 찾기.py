from itertools import permutations
import math

def solution(numbers):
    # 1. 모든 가능한 숫자 조합 만들기 (중복 제거를 위해 set 사용)
    p_set = set()
    
    # numbers는 문자열 그 자체로 반복문이 가능하므로 리스트화 안 해도 됨
    for i in range(1, len(numbers) + 1):
        list_i = permutations(numbers, i)
        for j in list_i:
            p_set.add(int(''.join(j)))

    # 2. 소수 개수 세기
    answer = 0
    for k in p_set:
        if k < 2:  # 0과 1은 소수가 아님
            continue
            
        is_prime = True
        # 소수 판별: 2부터 루트 k까지 나누어지는지 확인
        # range(2, int($\sqrt{k}$) + 1)
        for j in range(2, int(math.sqrt(k)) + 1):
            if k % j == 0:
                is_prime = False
                break
        
        if is_prime:
            answer += 1
                
    return answer