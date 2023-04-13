import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

answer = []
n=int(input())
dic = defaultdict(list)
for i in range(1,n+1):
    num, start, finish = map(int, input().split())
    dic[num] = [start, finish]
sortDic = sorted(dic.items(), key=lambda x:(x[1]))
for c in sortDic:
    if answer:
        if c[1][0]>=answer[0]:
            heappop(answer)
    heappush(answer, c[1][1])
print(len(answer))