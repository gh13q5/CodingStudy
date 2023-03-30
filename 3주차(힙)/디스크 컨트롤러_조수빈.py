import heapq
def solution(jobs): #처음에는 실행시간 - 대기시간 으로 우선순위 결정... 근데 그냥 실행시간만 고려하면 되더라
    answer = 0
    time = 0
    n = len(jobs) #작업의 갯수
    while len(jobs) != 0:
        #현재 시점에 대기하고있는 목록 필터링. 실행시간 기준 최소힙이니까 reversed사용하여 각 요소의 앞뒤를 바꿔줌.
        request =list(list(reversed(x)) for x in jobs if x[0]<=time)
        
        if len(request) != 0:
            heapq.heapify(request)#대기 리스트를 힙으로 정렬
            now = heapq.heappop(request)#가장 실행시간 짧은 작업 수행
            answer += (time-now[1]+now[0])#작업시간 총 합에 현재 실행한 작업 시간 더함
            time += now[0]#현재 작업이 종료되는 시점으로 이동
            jobs.remove(list(reversed(now)))#작업 목록에서 지금 수행한 작업 제거
        else:
            time += 1
    
    answer = answer//n #처음에는 작대기 하나만 써서 오류남... 정수형으로 나머지 버리는 나눗셈 하려면 작대기 두개
    return answer
