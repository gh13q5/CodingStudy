from functools import cmp_to_key

def comp(x, y):
    if x[0] == y[0]:
        if int(y+x) > int(x+y):
            return 1
        else:
            return -1
    else:
        if x[0] < y[0]:
            return 1
        else:
            return -1
            
def solution(numbers):
    answer = ''
    nm = [str(n) for n in numbers]
    sorted_list = sorted(nm, key=cmp_to_key(comp))
    
    for s in sorted_list:
        answer+=s
    
    if int(answer) == 0:
        return '0'

    return answer
