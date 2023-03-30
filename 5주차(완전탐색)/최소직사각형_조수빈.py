def solution(sizes):
    answer = 0
    an = [a.sort() for a in sizes]
    a1 = 0
    a0 = 0
    for a in sizes:
        if a[0] > a0:
            a0 = a[0]
        if a[1] > a1:
            a1 = a[1]
    answer = a1*a0
    return answer
