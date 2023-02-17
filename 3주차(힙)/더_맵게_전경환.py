def solution(scoville, K):
    import heapq
    
    answer = 0
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
            sf = heapq.heappop(scoville) + ((heapq.heappop(scoville))*2)
            cnt += 1
            heapq.heappush(scoville, sf)
            
            if len(scoville) == 1 and scoville[0] < K:
                return -1
    
    answer = cnt

    return answer
    
