from collections import defaultdict
from collections import deque
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import heapq
def solution(k, n, reqs):
    d = defaultdict(list)
    waiting = [[i,0] for i in range(1, k+1)]
    rest = n - k
    mentos = [1 for _ in range(k)]
    candList = []
    
    mentosList = set()
    for comb in combinations_with_replacement([i for i in range(1, n - k + 2)], r=k):
        if sum(comb) == n:
            for perm in permutations(comb, k):
                mentosList.add(perm)
                
    for req in reqs:
        d[req[2]].append([req[0],req[1]])
    
    for mentos in mentosList:
        cand = 0
        waiting = [[i,0] for i in range(1, k+1)]
        for i in range(1, k+1):
            waitingTime = 0
            mentoNum = mentos[i-1]
            q = []
            for r in d[i]:
                if len(q) < mentoNum:
                    finTime = r[0] + r[1]
                    heapq.heappush(q, finTime)
                else:
                    out = heapq.heappop(q)
                    if r[0] < out:
                        waitingTime += out - r[0]
                        finTime = out + r[1]
                    else:
                        finTime = r[0]+r[1]
                    heapq.heappush(q, finTime)
            waiting[i-1][1] = waitingTime
        for wait in waiting:
            cand += wait[1]
        candList.append(cand)
    candList.sort()
    return candList[0]