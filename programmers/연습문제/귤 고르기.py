def solution(k, tangerine):
    answer = 0
    
    tangerine.sort()
    sort_tang = []
    cnt = 0
    for i in range(len(tangerine)):
        cnt += 1
        if i != len(tangerine) - 1:
            if tangerine[i] != tangerine[i+1]:
                sort_tang.append(cnt)
                cnt = 0
        else:
            if tangerine[i-1] != tangerine[i]:
                sort_tang.append(cnt-1)
                sort_tang.append(1)
            else:
                sort_tang.append(cnt)
                
    sort_tang.sort()
    sort_tang.reverse()
    idx = 0
    while(k>0):
        answer += 1
        k -= sort_tang[idx]
        idx += 1
    return answer