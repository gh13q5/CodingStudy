def solution(clothes):
    
    answer = 1
    
    d_clothes = dict(clothes)
    d_t = {values:0 for values in d_clothes.values()}
    
    for i in clothes:
        if i[1] in d_t.keys():
            d_t[i[1]] += 1
        else:
            d_t[i[1]] = 1
    
    for i in d_t:
        print(d_t[i])
        answer *= (d_t[i]+1)
        
        
    return answer-1
