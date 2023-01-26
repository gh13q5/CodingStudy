def solution(clothes):
    items={}
    answer = 1
    
    for item, category in clothes:
        if category not in items:
            items[category] = []
        items[category].append(item)
        
    for x in items.keys():
        answer *= len(items[x]) + 1
    
    return answer - 1
