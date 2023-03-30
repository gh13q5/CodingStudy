def solution(word):
    answer = 0
    d = ['A','E','I','O','U']
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * d.index(n) + 1
    return answer
