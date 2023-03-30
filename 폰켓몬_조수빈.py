def solution(nums):
    answer = 0
    qnt = len(nums)/2
    sp = set(nums)
    if(len(sp)<qnt):
        answer = len(sp)
    else:
        answer = qnt
    return answer
