from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d= deque()
for i in range(1, n+1):
    d.append(i)
idx = list(map(int,input().split()))
answer = 0
cnt = 0
while cnt < m:
    if d[0] == idx[cnt]:
        d.popleft()
        cnt += 1
    else:
        dif = d.index(idx[cnt])
        if dif > len(d)//2:
            d.rotate(len(d)-dif)
            answer += len(d)-dif
        else:
            d.rotate(-1*dif)
            answer += dif

print(answer)
