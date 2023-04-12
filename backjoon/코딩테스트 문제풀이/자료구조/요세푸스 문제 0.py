from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d= deque()
answer = []
for i in range(1, n+1):
    d.append(i)
while len(d):
    d.rotate(-1*k+1)
    answer.append(d.popleft())
print('<', end='')
for i in range(n-1):
    print(str(answer[i]) + ',', end=' ')
print(str(answer[-1])+'>')
