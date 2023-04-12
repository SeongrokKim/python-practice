from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int,input().split())
weight = deque(map(int,input().split()))
road = deque()
timer = deque()
answer = 0
while len(weight)>0 or len(road)>0:
    if len(timer):
        if timer[0] > w - 1:
            timer.popleft()
            road.popleft()
        for i in range(len(timer)):
            timer[i] += 1
    if len(road)<w:
        if len(weight):
            if sum(road) + weight[0] <= L:
                road.append(weight.popleft())
                timer.append(1)
    answer += 1
print(answer)
        