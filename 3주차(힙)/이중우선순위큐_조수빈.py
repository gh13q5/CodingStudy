from heapq import heappush, heappop
def solution(operations):
    answer = []
    min_heap = []#최소힙
    max_heap = []#최대힙
    for op in operations:
        opt = op.split()#문자열 슬라이싱
        if opt[0] == "I":#명령어가 I일때
            heappush(min_heap,int(opt[1]))
            heappush(max_heap,(-int(opt[1]),int(opt[1])))#최소,최대힙에 각각 주어진 숫자 삽입
        elif len(min_heap) != 0:#명령어가 D이고 현재 힙에 원소가 있을 때
            if opt[1] == '1':
                min_heap.remove(heappop(max_heap)[1])#max힙을 pop하여 최댓값 제거 후 최소힙에서도 같은 원소 제거
            else:
                m = heappop(min_heap)#최소힙을 pop하여 최솟값 제거 후
                max_heap.remove((-m,m))#최대힙에서도 같은 원소 제거
    
    if len(min_heap) == 0:#힙에 원소가 남아있지 않으면
        return [0,0]
    else:
        return[heappop(max_heap)[1],heappop(min_heap)]#힙에 원소가 남아있으면
        
    return answer
