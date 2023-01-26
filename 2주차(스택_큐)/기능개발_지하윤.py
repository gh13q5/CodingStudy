import math
def solution(progresses, speeds):
    answer = []
    time = []
    idx = 0
    
    #각 기능마다 소요되는 시간 구해서 time 배열에 넣기
    for i, v in enumerate(progresses):
        time.append(math.ceil((100-v)/speeds[i]))
    
    # 처음엔 각각의 데이터를 카운트했지만 예외가 발생해서 접근법 변경!
    # 배열 인덱스를 이용해서 갯수 구함
    for i in range(len(time)):
        if time[i] > time[idx]:  
            answer.append(i - idx)
            idx = i # 소요시간이 큰 값으로 업데이트
    answer.append(len(time) - idx)  
        
    return answer

# 테스트2만 오류가 났었는데 위 접근법과는 관계없는 문제로, 소요시간의 소수점 처리를 하지않아서 생긴 문제였음!
