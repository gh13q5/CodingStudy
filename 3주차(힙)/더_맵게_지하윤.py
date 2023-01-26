import heapq

def solution(scoville, K):
    answer = 0
    
    # 힙 큐 만들기
    heapq.heapify(scoville)
        
    while True:
        notSpicy = heapq.heappop(scoville)
        if ( notSpicy >= K ): return answer      # 모두 기준을 넘었을 때
    
        try:
            # 가장 맵지 않은 두 개의 음식 섞어서 저장
            heapq.heappush(scoville, notSpicy + heapq.heappop(scoville)*2)
        except:
            return -1                            # 원소가 낫스파이시 하나 뿐일 때
        
        answer+=1
        
    return answer
