def solution(nums):
    # 1. 딕셔너리(해시)를 이용해 폰켓몬 종류별로 분류합니다.
    hash_dict = {}
    for n in nums:
        hash_dict[n] = 1 # 값은 중요하지 않음, 키가 중복을 막아줌
        
    # 2. 총 몇 종류인지 계산합니다.
    variety = len(hash_dict)
    
    # 3. 내가 가져갈 수 있는 최대치(N/2)와 종류 수 중 작은 값을 선택합니다.
    pick_limit = len(nums) // 2
    
    return min(variety, pick_limit)