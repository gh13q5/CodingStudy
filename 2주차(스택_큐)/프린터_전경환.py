def solution(priorities, location):
    from collections import deque
    answer = 0
    idxs = list(range(len(priorities)))
    # 중요도의 길이만큼의 index로 구성된 리스트 생성
    dic = {key: values for key, values in zip(idxs, priorities)}
    # index를 key, 중요도를 value로 하여 딕셔너리 생성
    que = deque(dic.items())
    # (key, value) 로 deque 생성
    cnt = 0
    while len(que):
        # que의 길이가 0이 될 때까지 반복
        item = que.popleft()
        # item은 que의 왼쪽에서 pop한 것. que[0]
        if any(item[1] < q[1] for q in que):
            # item[1](que[0]의 중요도)가 que[1](que의 나머지 중요도) 보다 작다면
            que.append(item)
            # 맨 뒤에 다시 삽입
        else:
            # 가장 중요도가 높다면
            cnt += 1
            # 인쇄, cnt(인쇄된 순서)에 + 1
            if item[0] == location:
                # item의 인덱스가 location과 같다면 (내가 요청 문서라면)
                answer = cnt
                return answer
                # 인쇄된 순서 반환
