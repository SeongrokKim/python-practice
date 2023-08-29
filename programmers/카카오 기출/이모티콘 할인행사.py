from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    salePercent = [10, 20, 30, 40]
    menu = [[] for _ in range(len(emoticons))]
    for i in range(len(emoticons)):
        for j in range(4):
            menu[i].append((salePercent[j], int(emoticons[i]//10*(10-salePercent[j]*0.1))))
    comb = list(product(*menu))
    for com in comb:
        totList = [0 for _ in range(len(users))]
        serviceUser = 0
        margin = 0
        for i in range(len(users)):
            tot = 0
            for c in com:
                if c[0] >= users[i][0]:
                    tot += c[1]
            if tot >= users[i][1]:
                serviceUser += 1
                tot = 0
            totList[i] = tot
        margin = sum(totList)
        if serviceUser > answer[0]:
            answer = [serviceUser, margin]
        elif serviceUser == answer[0]:
            answer = [serviceUser, max(margin, answer[1])]
    return answer