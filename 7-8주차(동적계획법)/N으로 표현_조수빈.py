def operate(a, b):
    n_set = set()
    for x in a:
        for y in b:
            n_set.add(x+y)
            n_set.add(x-y)
            n_set.add(y-x)
            n_set.add(x*y)
            if y != 0:
                n_set.add(x//y)
            if x != 0 :
                n_set.add(y//x)
    return n_set
def solution(N, number):
    answer = -1
    memoz = []
    if number == N:
        return 1
    else:
        memoz.append([N])
    for i in range(2,9):
        if N*int('1'*i) == number:
            return i
        setlist = set()
        setlist.add(N*int('1'*i))
        j = 1
        while j < i//2+1:
            setlist.update(operate(memoz[j-1],memoz[i-j-1]))
            j+=1
        if number in list(setlist):
            return i
        else:
            memoz.append(list(setlist))
            
    return answer
