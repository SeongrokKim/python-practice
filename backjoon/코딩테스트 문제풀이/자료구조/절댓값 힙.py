from heapq import heapify, heappop, heappush
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
heap = []
dic = defaultdict(list)
for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            minval = heappop(heap)
            print(min(dic[minval]))
            dic[minval].remove(min(dic[minval]))
    else:
        heappush(heap, abs(x))
        dic[abs(x)].append(x)
    