def solution(n, costs):
    answer = 0
    #부모 노드 초기화
    parents = [i for i in range(n)]
    def findParent(parents,x):
        if parents[x] != x:
            parents[x] = findParent(parents,parents[x])
        return parents[x]
    
    def unionParent(parents,a,b):
        a = findParent(parents,a)
        b = findParent(parents,b)
        
        if a > b :
            parents[b] = a
        else:
            parents[a] = b
    
    costs.sort(key = lambda x : x[2])
    
    for a,b,c in costs:
        if findParent(parents,a) != findParent(parents,b):
            unionParent(parents,a,b)
            answer += c
    return answer
