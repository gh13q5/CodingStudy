def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        genre = genres[i]
        if genre not in dic:
            dic[genre] = [plays[i], (plays[i], i)]
        else:
            dic[genre][0] += plays[i]
            dic[genre].append((plays[i], i))

    temp = []
    for d in dic.values():
        temp.append(d)

    temp.sort(reverse=True)

    temp1 = []
    for t in temp:
        temp1.append(sorted(t[1:], key=lambda x: (x[0], -x[1]), reverse=True))

    for t in temp1:
        if len(t) == 1:
            answer.append(t[0][1])
        else:
            answer.append(t[0][1])
            answer.append(t[1][1])

    return answer
