def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    while routes:
        answer+=1
        pi = routes.pop(0)
        while routes and routes[0][0] <= pi[1]:
            routes.pop(0)
    return answer
