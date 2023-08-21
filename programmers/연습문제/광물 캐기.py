from collections import deque
def solution(picks, minerals):
    answer = 0
    totPicks = sum(picks)
    maxMinerals = totPicks*5
    numOfMinerals = len(minerals)
    if numOfMinerals > maxMinerals:
        minerals = minerals[:maxMinerals].copy()
        print(minerals)
    q = len(minerals) // 5
    r = len(minerals) % 5
    l = []
    setNum = 0
    for i in range(q):
        counts = [0,0,0]
        for j in range(5):
            if minerals[i*5+j] == 'diamond':
                counts[0] += 1
            elif minerals[i*5+j] == 'iron':
                counts[1] += 1
            elif minerals[i*5+j] == 'stone':
                counts[2] += 1
        l.append((setNum,counts))
        setNum += 1
    counts = [0,0,0]
    if q*5 < len(minerals):
        for i in range(q*5, len(minerals)):
            if minerals[i] == 'diamond':
                counts[0] += 1
            elif minerals[i] == 'iron':
                counts[1] += 1
            elif minerals[i] == 'stone':
                counts[2] += 1
        l.append((setNum,counts))
    l.sort(key=lambda x:(x[1][0], x[1][1], x[1][2]), reverse=True)
    ll = deque()
    for i in range(len(l)):
        ll.append(l[i])
    
    idx = 0
    while ll:
        if picks[idx]:
            if idx == 0:
                answer += sum(ll[0][1])
            elif idx == 1:
                answer += ll[0][1][0]*5+ll[0][1][1]+ll[0][1][2]
            elif idx == 2:
                answer += ll[0][1][0]*25+ll[0][1][1]*5+ll[0][1][2]
            picks[idx] -= 1
            ll.popleft()
        else:
            idx += 1
                
    return answer