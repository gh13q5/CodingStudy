def solution(genres, plays):
    answer = []
    g_plays = {}
    
    tp = list(zip(range(len(genres)),genres,plays))
    
    for x in tp:
        if x[1] in g_plays:
            p = g_plays[x[1]]
            sum = p + x[2]
            g_plays[x[1]] = sum
        else:
            g_plays[x[1]] = x[2]
    
    
    g_sorted = sorted(list(zip(g_plays.keys(),g_plays.values())), key = lambda x:-x[1])
    
    for g in g_sorted:
        temp = list(filter(lambda x : x[1] == g[0], tp))
        temp2 = sorted(temp, key = lambda x:(-x[2],x[0]))
        for t in range(len(temp2)):
            if(t >= 2):
                continue
            else:
                answer.append(temp2[t][0])
        
    
    return answer
