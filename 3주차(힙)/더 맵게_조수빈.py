import heapq 
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)#최소힙 생성
    while len(scoville) != 0 :
        s = heapq.heappop(scoville)#가장 맵지 않은 음식
        if s >= K:#섞기전에 최솟값이 목표를 충족하면 횟수 리턴
            return answer
        else:
            if len(scoville) == 0 :#목표값 도달 못했는데 힙에 요소가 없으면 -1리턴
                return -1
            else:
                answer +=1 #횟수 증가
                s+=(heapq.heappop(scoville)*2)#다음 매운맛 추출후 섞기
                heapq.heappush(scoville,s)#힙에 삽입
    return -1
