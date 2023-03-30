def solution(clothes):
    answer = 1
    dict_c = dict(clothes)
    v = list(dict_c.values())
    s = list(set(v))
    
    for i in range(len(s)):
        cnt = v.count(s[i]) + 1
        answer *= cnt
        
    
    return answer - 1
