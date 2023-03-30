def solution(numbers, target):
    answer = 0
    memo = [[] for num in numbers]
    memo[0].append(-numbers[0])
    memo[0].append(numbers[0])
    for i in range(1,len(numbers)):
        for t in memo[i-1]:
            memo[i].append(t+numbers[i])
            memo[i].append(t - numbers[i])
    
    answer = memo[-1].count(target)
    return answer
