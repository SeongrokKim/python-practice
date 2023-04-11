def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = 1
        else:
            dic[cloth[1]] += 1
    numList = list(dic.values())
    
    for i in range(len(numList)):
        answer *= (numList[i] + 1)
    return answer-1