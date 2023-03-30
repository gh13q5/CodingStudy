from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    sum_b = 0
    bridge_now = deque([0 for i in range(bridge_length)])
    d_trucks = deque(truck_weights)
    a_trucks = deque(truck_weights)
    while len(a_trucks) != 0:
        arrive = bridge_now.pop()
        sum_b -= arrive
        
        if len(d_trucks) != 0 and sum_b + d_trucks[0] <= weight:
            n = d_trucks.popleft()
            bridge_now.appendleft(n)
            sum_b += n
        else:
            bridge_now.appendleft(0)
        
        if arrive != 0:
            a_trucks.popleft()
        
        answer += 1
        
    return answer
