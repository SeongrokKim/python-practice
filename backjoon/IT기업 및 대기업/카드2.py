from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()
for i in range(1, n+1):
    d.appendleft(i)

while len(d) > 1:
    d.pop()
    d.appendleft(d.pop())
print(d.pop())