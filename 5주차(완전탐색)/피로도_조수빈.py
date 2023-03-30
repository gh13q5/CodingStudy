from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for pe in permutations(dungeons, len(dungeons)):
        result = 0
        now = k
        for p in pe:
            if p[0]<=now:
                result+=1
                now -= p[1]
        if result > answer:
            answer = result
    return answer
