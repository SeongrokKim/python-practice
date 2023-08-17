import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,-1,0,1] #상,좌,하,우
lake = []
pos = []
water = deque()
day = 0

for i in range(r):
    state = list(input())
    for j in range(c):
        if state[j] == '.' or state[j] == 'L':
            water.append((i,j))
        if state[j] == 'L':
            pos.append((i,j))
    lake.append(state)

visited = [[0 for _ in range(c)] for _ in range(r)]
queue = deque()
x,y = pos[0][0], pos[0][1]
queue.append((x,y))
visited[x][y] = 1

def bfs(lake, visited, queue):
    next_queue = deque()
    while queue:
        now = queue.pop()
        if now[0] == pos[1][0] and now[1] == pos[1][1]:
            return True, None
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx > -1 and nx < r and ny > -1 and ny < c:
                if visited[nx][ny] == 0:
                    if lake[nx][ny] == 'X':
                        next_queue.appendleft((nx,ny))
                    else:
                        queue.appendleft((nx,ny))
                    visited[nx][ny] = 1
    return False, next_queue

def melting(water, lake):
    next_water = deque()
    while water:
        x, y = water.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > -1 and nx < r and ny > -1 and ny < c:
                if lake[nx][ny] == 'X':
                    next_water.appendleft((nx,ny))
                    lake[nx][ny] = '.'
    return next_water

while True:
    state, next_queue = bfs(lake, visited, queue)
    if state:
        break
    day += 1
    water = melting(water, lake)
    queue = next_queue

print(day)
