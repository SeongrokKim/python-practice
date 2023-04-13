def solution(brown, yellow):
    answer = []
    tot = brown + yellow
    totdiv = []
    for i in range(3, tot+1):
        if tot%i == 0:
            totdiv.append(i)
    for s in totdiv:
        g = tot//s
        if (s-2)*(g-2) == yellow:
            return [g, s]
        
    return answer