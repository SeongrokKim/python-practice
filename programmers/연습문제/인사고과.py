def solution(scores):
    answer = 1
    num = len(scores)
    rank = []
    wanhoA=scores[0][0]
    wanhoB=scores[0][1]
    for i, s in enumerate(scores):
        rank.append([sum(s), s[0], s[1], i])
    sortRank = sorted(rank, key=lambda x:(-x[1],x[2]))
    t = 0
    for score in sortRank:
        if wanhoA < score[1] and wanhoB < score[2]:
            return -1
        if t<=score[2]:
            if wanhoA+wanhoB < score[1] + score[2]:
                answer += 1
            t = score[2]
                    
    return answer