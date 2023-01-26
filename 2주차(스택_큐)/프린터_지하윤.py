def solution(priorities, location):
    index_list = [index for index in range(len(priorities))]
    
    i = 0
    while True:
        if (priorities[i] < max(priorities[(i+1):])):
            #i 다음 인덱스부터 작을 경우, 다시 뒤로 넣음
            priorities.append(priorities.pop(i))
            index_list.append(index_list.pop(i))
        else:
            i += 1
            
        if (priorities == sorted(priorities, reverse=True)): break
        
            
    return index_list.index(location)+1

# location의 위치 팔로업 하는 것 때문에 좀 헤맸는데 index를 따로 저장하는 리스트를 만들어서 함께 돌림
# .index 메소드 사용해서 location의 현재위치를 알아냄

# 처음 오류
    # 최댓값과 일치해서 첫 출력인 경우
    # if(priorities[location] == max(priorities)): return 1
    # 이런 부분을 넣었는데 동일한 값이 여러개 있을 가능성을 고려하지 못했기 때문에 제거하고 해결
    
