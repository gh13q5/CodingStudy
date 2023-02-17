def solution(progresses, speeds):
    import math
    from collections import deque
    answer = []
    day = 0
    days = deque()
    cnt = 0
    for i in range(len(progresses)):
        # progresses의 길이만큼 반복
        day = math.ceil((100 - progresses[i])/speeds[i])
        # 배포 가능한 날 = 100 - (작업진도 / 작업속도) math.ceil을 이용하여 올림
        days.append(day)
        # 배포 가능한 날로 deque 생성
        
    while days:
        # days가 0이 될 때까지 반복
        cnt = days.popleft()
        # cnt는 days에서 왼쪽으로 pop한 값 = days[0]
        f = 1
        # f는 배포되는 기능의 수 / 기본값 1
        while days and cnt >= days[0]:
            # days와 cnt가 days[0]보다 크거나 같다면 반복
            days.popleft()
            # days pop
            f += 1
            # 배포 되는 기능 수 + 1
        answer.append(f)
        # 배포 되는 기능 수로 리스트 생성
    return answer
