from collections import deque
def solution(progresses, speeds):
    answer = []
    pq = deque(progresses)
    sq = deque(speeds)
    n = 1
    while len(pq) != 0 :
        if (pq[0] + sq[0] * n) >= 100 :
            i = 0
            
            while (len(pq) != 0 and pq[0] + sq[0] * n) >= 100:
                pq.popleft()
                sq.popleft()
                i+=1
            answer.append(i)
        n+=1
                
                
                
    return answer
