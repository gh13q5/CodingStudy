def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    dic ={}
    
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
                      
    for i in completion:
        if i in dic:
            dic[i] -=1
    
    for key, values in dic.items():
        if values != 0:
            answer = key
    
    return answer
    
