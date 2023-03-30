from collections import deque
def solution(maps):
    answer = -1
    x = len(maps[0])
    y = len(maps)
    queue = deque()
    queue.append((0,0,1))
    while queue:
        k = queue.popleft()
        i = k[0]
        j = k[1]
        
        if (y-1,x-1) == (i,j):
            return k[2]
        
        if maps[i][j] == 0:
            continue
        maps[i][j] = 0
        
        if j > 0:
            queue.append((i,j-1,k[2]+1))
        if i > 0:
            queue.append((i-1,j,k[2]+1))
        if i < y-1:
            queue.append((i+1,j,k[2]+1))
        if j < x-1:
            queue.append((i,j+1,k[2]+1))
        
    return -1
