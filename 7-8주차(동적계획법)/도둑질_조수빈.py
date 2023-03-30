def solution(money):
    answer = 0
    g1 = money[:-1].copy()
    g2 = money[1:].copy()
    
    for g in range(1,len(g1)):
        if g == 1:
            temp = max(g1[1],g1[0])
            g1[1] = temp
        else:
            temp = max(g1[g-1],g1[g-2] + g1[g])
            g1[g] = temp
    
    for g in range(1,len(g2)):
        if g == 1:
            temp = max(g2[1],g2[0])
            g2[1] = temp
        else:
            temp = max(g2[g-1],g2[g-2] + g2[g])
            g2[g] = temp
    
    answer = max(g1[-1],g2[-1])
        
    return answer
