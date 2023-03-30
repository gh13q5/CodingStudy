def solution(n, times):
    answer = 0
    
    minn = times[0]
    maxx = times[0]*n
    
    while 1 :
        mid = (minn + maxx) // 2
        count = 0
        
        for t in times:
            count += mid // t
        
        if count >= n :
            maxx = mid
        if count < n:
            minn = mid
        
        if minn == maxx-1:
            return maxx
                
    return answer
