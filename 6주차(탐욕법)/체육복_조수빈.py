import copy
def solution(n, lost, reserve):
    answer = 0
    #여벌옷 가져온 애들 중 도난당한애들 제거
    lost2 = [x for x in lost if x not in reserve]
    reserve2 = [x for x in reserve if x not in lost]
    reserve3 = copy.deepcopy(reserve2)
    answer2 = 0

    for l in lost2:
        if l + 1 in reserve2:
            answer+= 1
            reserve2.remove(l + 1)
        elif l - 1 in reserve2:
            answer += 1
            reserve2.remove(l - 1)

    for l in lost2:
        if l - 1 in reserve3:
            answer2 += 1
            reserve3.remove(l - 1)
        elif l + 1 in reserve3:
            answer2 += 1
            reserve3.remove(l + 1)

    if answer < answer2:
        return n - len(lost2) + answer2


    return n - len(lost2) + answer
