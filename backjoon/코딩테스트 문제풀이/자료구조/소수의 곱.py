import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

k, n = map(int,input().split())
heap = list(map(int, input().split()))
tmp = []
for i in range(len(heap)):
    tmp.append(heap[i])
heapify(heap)
maxval = max(heap)
for j in range(n-1):
    small = heappop(heap)
    for i in range(len(tmp)):
        heappush(heap, tmp[i]*small)
        if small%tmp[i] == 0:
            break
print(heappop(heap))