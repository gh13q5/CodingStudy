def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    a1 = 0
    a2 = 0 
    a3 = 0 #아예 처음부터 맞춘 개수 리스트로 선언했으면 더 깔끔했을듯....
    for a in range(len(answers)):
        try:
            if s1[a%len(s1)] == answers[a]:
                a1 += 1
            if s2[a%len(s2)] == answers[a]:
                a2 += 1
            if s3[a%len(s3)] == answers[a]:
                a3 += 1
        except:
            if s1[0] == answers[a]:
                a1 += 1
            if s2[0] == answers[a]:
                a2 += 1
            if s3[0] == answers[a]:
                a3 += 1
    
    alist = [a1,a2,a3]
    
    m = max(alist)
    answer = [x+1 for x,v in enumerate(alist) if v == m]
        
    return answer
