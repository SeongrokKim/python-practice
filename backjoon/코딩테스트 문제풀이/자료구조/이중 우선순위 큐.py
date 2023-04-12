import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

def pop(heap):
    while len(heap)>0:
        data, id = heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data
    return None

t= int(input())
for _ in range(t):
    k = int(input())
    minq = []
    maxq = []
    cnt = 0
    deleted = [False] * (k+1)
    for _ in range(k):
        command = input().split()
        if command[0] == 'I':
            heappush(minq, (int(command[1]), cnt))
            heappush(maxq, (-1*int(command[1]), cnt))
            cnt += 1
        else:
            if command[1] == '1':
                pop(maxq)
            else:
                pop(minq)
                    
    maxval = pop(maxq)
    if maxval!=None:
        heappush(minq, (-maxval,cnt))
        print(-maxval, pop(minq))
        
    else:
        print("EMPTY")