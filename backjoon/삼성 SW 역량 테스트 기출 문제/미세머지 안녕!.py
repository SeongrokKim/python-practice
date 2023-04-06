from collections import deque
r,c,t = map(int, input().split())

room = []
for i in range(r):
    tmp = list(map(int,input().split()))
    room.append(tmp)

for i in range(r):
    if room[i][0] == -1:
        gc1 = i
        gc2 = i+1
        break

def diffusion():
    
    pass

def operation():
    pass

cnt = 0
while cnt<t:
    diffusion()
    operation()
    cnt += 1
