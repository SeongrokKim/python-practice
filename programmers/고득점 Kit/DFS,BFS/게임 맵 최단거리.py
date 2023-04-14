from collections import deque
def solution(maps):
    answer = 0
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    d = deque()
    d.append([0,0,1])
    visited[0][0] = 1
    cnt = 1
    while d:
        now = d.popleft()
        if now[0] == len(maps)-1 and now[1] == len(maps[0])-1:
            break
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or visited[nx][ny] or maps[nx][ny] == 0:
                continue
            else:
                d.append([nx,ny,now[2]+1])
                visited[nx][ny] = 1
                
    if visited[len(maps)-1][len(maps[0])-1]:
        return now[2]
    else:
        return -1