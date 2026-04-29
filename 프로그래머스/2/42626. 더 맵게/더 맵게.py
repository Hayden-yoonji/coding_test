from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        min1 = heappop(scoville)
        min2 = heappop(scoville)
        new = min1 + min2*2
        answer += 1
        heappush(scoville, new)
        
    return answer