import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

t= int(input())
for _ in range(t):
    m = int(input())
    l = []
    h = []
    if m>10:
        for i in range((m-1)//10+1):
            l += list(map(int,input().split()))
    else:
        l += list(map(int,input().split()))
    print((m+1)//2)
    cycle = 0
    while 20*cycle+20 <= m:
        for i in range(20*cycle, 20*cycle+20):
            h.append(l[i])
            h.sort()
            if i%2==0:
                print(h[i//2], end=' ')
        print()
        cycle += 1
    if 20*cycle+20>m:
        for i in range(20*cycle, m):
            h.append(l[i])
            h.sort()
            if i%2==0:
                print(h[i//2], end=' ')
    print()
    
