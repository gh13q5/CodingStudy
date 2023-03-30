def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for t in range(i+1):
            if t == 0:
                triangle[i][0] +=  triangle[i-1][0]
            elif t == i:
                triangle[i][t] += triangle[i-1][-1]
            else:
                triangle[i][t] += max((triangle[i-1][t-1],triangle[i-1][t]))
    answer = max(triangle[-1])
            
    return answer
