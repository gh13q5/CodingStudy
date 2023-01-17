def solution(nums):
    answer = 0
    sel_n = len(nums)//2
    kind = len(set(nums))
    
    if sel_n == kind:
        answer = kind
    elif kind > sel_n:
        answer = sel_n
    else:
        answer = kind

    return answer
