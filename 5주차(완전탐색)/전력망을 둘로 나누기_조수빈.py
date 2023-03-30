import copy
from collections import deque
def bfs(node, t, n):
        visited = [0] * (n+1)
        q = deque([node])
        visited[node] = 1
        cnt = 1
        while q:
            v = q.popleft()
            for i in t[v]:
                if visited[i] != 1:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
                
        return cnt
def solution(n, wires):
    answer = n
    tree = [[]for i in range(n+1)]
    
    for a,b in wires:
        tree[a].append(b)
        tree[b].append(a)
    
    
    
    for a,b in wires:
        t = copy.deepcopy(tree)
        t[a].remove(b)
        t[b].remove(a)
        
        temp = abs(bfs(a,t,n)-bfs(b,t,n))
        if answer > temp:
            answer = temp
        
    return answer
#bfs 쓰기전에 풀려고했던방법: 현재 끊는 와이어랑 연결된 노드로 집합 두개 만듬->wires 없어질때까지 무한루프 돌면서 ... 노드들이랑 이어진 와이어 보이면 와이어 flat해서 해당 노드 있는 집합에 집어넣음. 근데 이거 너무오래걸릴것같아서 bfs로,,,, 
