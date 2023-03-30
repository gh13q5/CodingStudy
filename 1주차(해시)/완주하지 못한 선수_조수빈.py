from collections import Counter
def solution(participant, completion):
    answer = ''
    hash_participant = Counter(participant)
    hash_completion = Counter(completion)
    for x in participant:
        if(hash_participant[x] != hash_completion[x]):
            answer = x
    return answer
