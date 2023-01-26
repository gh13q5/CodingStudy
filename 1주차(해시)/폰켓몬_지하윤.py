def solution(nums):
    hashDict = {}
    
    for num in nums:
        hashDict[hash(num)] = num
    
    poke = len(hashDict.keys())
    
    if len(nums)/2 >= poke:
        return poke
    else:
        return len(nums)/2
