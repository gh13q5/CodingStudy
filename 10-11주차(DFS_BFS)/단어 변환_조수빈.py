from collections import deque
def solution(begin, target, words):
    def mat(now,nex):
        r = []
        for i,b in enumerate(now):
            t = ''.join(now[j] for j in range(len(now)) if j != i)
            for w in nex:
                x = ''.join(w[j] for j in range(len(w)) if j != i)
                if x == t:
                    r.append(w)
        return r
    
    answer = 0
    visited = []
    queue = deque([(begin,0)])
    
    while queue:
        b = queue.popleft()
        visited.append(b[0])
        k = mat(b[0],list(set(words) - set(visited)))
        if target in k:
            return b[1] + 1
        else:
            for t in k:
                queue.append((t,b[1]+1))
        
    return answer
