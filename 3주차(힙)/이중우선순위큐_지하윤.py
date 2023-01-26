import heapq

def solution(operations):
    maxnum = []
    minnum = []
    total = []
    answer = [0, 0]
    
    for oper in operations:
        current = oper.split()
        # I
        if current[0] == "I":
            heapq.heappush(maxnum, (-int(current[1]), int(current[1])))
            heapq.heappush(minnum, int(current[1]))
            heapq.heappush(total, int(current[1]))
            continue
        # D-    
        elif current[1] == "-1":
            if len(total) == 0: continue
            heapq.heappop(minnum)
            heapq.heappop(total)
        # D
        else:
            if len(total) == 0: continue
            heapq.heappop(maxnum)[1]
            heapq.heappop(total)
            
        # 모두 비었을 때 - 다른 큐도 비워준다
        if len(total) == 0:
            for i in range(len(maxnum)):
                heapq.heappop(maxnum)
            for j in range(len(minnum)):
                heapq.heappop(minnum)
            
    if len(total) != 0:
        answer[0]=heapq.heappop(maxnum)[1]
        answer[1]=heapq.heappop(minnum)
        
    return answer
