from collections import deque
import sys
input = sys.stdin.readline

n=int(input())
d= deque()
numlist = list(map(int, input().split()))
answer = []
for i in range(n):
    d.append([numlist[i],i+1])
for i in range(n):
    answer.append(d[0][1])
    dis = d[0][0]
    d.popleft()
    if dis>0:
        d.rotate(1-dis)
    else:
        d.rotate(-1*dis)
for i in range(n-1):
    print(answer[i], end=' ')
print(answer[-1])