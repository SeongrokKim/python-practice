from collections import deque
import sys
input = sys.stdin.readline

s = input().rsplit()[0]
t = input().rsplit()[0]
q = deque()
q.append(t)
while q:
    now = q.popleft()
    if now == s:
        print(1)
        exit()
    elif len(now)>1:
        if now[-1] == 'A':
            q.append(now[:-1])
        if now[0] == 'B':
            now = list(now)
            now.reverse()
            q.append(''.join(now[:-1]))
print(0)