def solution(genres, plays):
    answer = []
    tot = {}
    dic = {}
    for i in range(len(plays)):
        if genres[i] not in tot:
            tot[genres[i]] = plays[i]
        else:
            tot[genres[i]] += plays[i]
        dic[i] = plays[i]
    tot_sort = sorted(tot.items(), key = lambda x: x[1], reverse = True)
    dic_sort = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    
    for i in range(len(tot_sort)):
        m = tot_sort[i][0]
        cnt = 0
        j = 0
        while cnt < 2:
            if j == len(dic_sort):
                break
            if genres[dic_sort[j][0]] == m:
                answer.append(dic_sort[j][0])
                cnt += 1
            j += 1
        
    return answer