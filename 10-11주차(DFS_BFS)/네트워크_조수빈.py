def solution(n, computers):
    answer = 0
    root = [n for n in range(n)]
    
    for i, com in enumerate(computers):
        minn = i
        for j in range(n):
            if com[j] == 1:
                minn = min(minn,root[j],root[i])
        for j in range(n):
            if com[j] == 1:
                root = [minn if k==root[i] or k==root[j] else k for k in root]
    answer = len(set(root))
    return answer
