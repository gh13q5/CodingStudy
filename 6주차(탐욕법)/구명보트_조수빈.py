from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    
    while people:
        boat = 0
        boat += people.popleft()
        if people and boat + people[-1] <= limit:
            people.pop()
        answer += 1
            
            
    return answer
