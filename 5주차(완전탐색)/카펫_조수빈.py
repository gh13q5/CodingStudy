def solution(brown, yellow):
    answer = []
    pnum=[]
    if yellow == 1:
        return [3,3]
    else:
        for i in range(1,yellow//2+1):
            if yellow % i == 0:
                pnum.append(i)
    for p in pnum:
        c = yellow//p + 2
        r = p
        if c*2 + p*2 == brown:
            return[c,p+2]
    return answer
