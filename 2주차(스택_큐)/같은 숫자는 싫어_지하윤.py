def solution(arr):
    answer = []
    j=0
    answer.append(arr[0])
    
    for i in range(len(arr)):
        if answer[j] != arr[i]:
            answer.append(arr[i])
            j += 1
            
    return answer
