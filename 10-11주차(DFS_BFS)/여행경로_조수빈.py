import collections
def solution(tickets):
    answer = []
    ti = collections.defaultdict(list)
    for t in tickets:
        ti[t[0]].append(t[1])
    
    for t in tickets:
        ti[t[0]].sort()
    q = collections.deque()
    q.append('ICN')
    while q:
        n = q[-1]
        if ti[n] != []:
            ne = ti[n].pop(0)
            q.append(ne)
            print(q)
        else:
            answer.append(q.pop())
            
        
        
    answer.reverse()
    return answer
