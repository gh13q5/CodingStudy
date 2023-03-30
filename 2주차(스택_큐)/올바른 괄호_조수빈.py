def solution(s):
    answer = True
    stack = []
    for a in s:
        if a == "(":
            stack.append(0)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        return False

    return True
