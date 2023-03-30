def solution(array, commands):
    answer = []
    for c in commands:
        sliced = sorted(array[c[0]-1:c[1]]) 
        print (sliced)
        answer.append(sliced[c[2]-1])
    return answer
