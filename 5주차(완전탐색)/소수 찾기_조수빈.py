from itertools import permutations
from functools import reduce
def isPrime(num):
    if num <= 1:
        return False
    if num == 2 :
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
        
def solution(numbers):
    answer = 0
    primelist = []
    for n in range(1,len(numbers)+1):
        for i in permutations(numbers, n):
            if isPrime(int(reduce(lambda x, y: x + y, i))) == True :
                primelist.append(int(reduce(lambda x, y: x + y, i)))
    
    primelist = list(set(primelist))
    answer = len(primelist)
        
    return answer
