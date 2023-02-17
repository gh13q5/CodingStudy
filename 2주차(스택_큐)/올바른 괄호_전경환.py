def solution(s):
    answer = True
    a = 0
    
    for i in range(len(s)):
        # s의 길이만큼 반복
        if s[i] == "(" :
            # s[i]가 ( 이면
            a += 1
            # a 에다 1을 더함
        elif s[i] == ")":
            # s[i]가 ) 이면
            a -= 1
            # a에서 1을 뺌
            if a == -1:
                # a가 -1일 경우 (")"가 먼저 열렸을 경우)
                answer = False
                # 올바르지 않은 괄호이니 False
    if a != 0 or s[0] == ")" or s[-1] == "(":
        # a가 0이 아니거나 (짝이 안맞거나)
        # s[0]이 ")" (처음부터 닫는 괄호가 나오거나)
        # s[-1]이 "(" (마지막에 여는 괄호가 나오거나)
        answer = False
        # 올바르지 않은 괄호이니 False

    return answer
