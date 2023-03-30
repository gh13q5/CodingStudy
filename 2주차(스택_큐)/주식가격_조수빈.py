from collections import deque
def solution(prices):
    answer = []
    d_pr = deque(prices)
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            if prices[j] < prices[i]:
                answer.append(j - i)
                break
            elif(j == len(prices) - 1):
                answer.append(j - i)
    return answer
