import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    jobsQ = []
    
    # 현 시점 기록하며 현재 가능한 작업만 넣기
    while i < len(jobs):
        for j in jobs:
            # 지나간 시점은 필터링 하면서 현재 수행 가능한 작업을 저장
            if(start < j[0] <= now):
                # 위치 바꿔서 삽입
                heapq.heappush(jobsQ, [j[1], j[0]])
        # 현재 작업할 수 있는게 있을 때
        if (len(jobsQ) > 0):
            # 현 작업
            current = heapq.heappop(jobsQ)
            # 소요되는 시간 더해서 업데이트
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            now += 1

    return answer//len(jobs)

# 지나간 시점에 대한 작업 없이 했더니 문제가 생김.
# start로 구분을 추가로 해줌
