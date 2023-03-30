from collections import deque
def solution(priorities, location):
    answer = 0
    deq = deque(list(zip(priorities,range(len(priorities)))))
    while len(deq) != 0: 
        if max(deq)[0] == deq[0][0]:
            if deq[0][1] == location:
                return answer + 1
            else:
                answer += 1
                deq.popleft()
        else:
            deq.rotate(-1)
    return answer
