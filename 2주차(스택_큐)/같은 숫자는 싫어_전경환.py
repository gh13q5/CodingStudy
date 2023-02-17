def solution(arr):
    answer = []
    answer.append(arr[0])
    # answer에 arr 첫번째 값 넣기
    for i in range(len(arr)-1):
        # index만큼 반복
        if arr[i] != arr[i+1]:
            # arr의 index i값과 i+1값이 다르면
            answer.append(arr[i+1])
            # arr에 index i+1 값 넣기
            
    return answer
