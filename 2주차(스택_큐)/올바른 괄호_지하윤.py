def solution(s):
    answer = True
    sum = 0
    
    for str in s:
        if s[0] != "(":
            return False
        if s[len(s)-1] != ")":
            return False
        if sum < 0 :
            return False
        if str == "(":
            sum += 1
        else: sum -= 1

    if sum != 0: answer = False
    
    return answer
