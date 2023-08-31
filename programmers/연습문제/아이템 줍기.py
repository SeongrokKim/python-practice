from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = [[0 for _ in range(101)] for _ in range(101)]
    board = [[0 for _ in range(101)] for _ in range(101)]
    for rect in rectangle:
        for j in range(4):
            rect[j] *= 2
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    for rect in rectangle:
        for i in range(rect[0], rect[2]+1):
            for j in range(rect[1], rect[3]+1):
                board[i][j] = 1
    
    for rect in rectangle:
        for i in range(rect[0]+1, rect[2]):
            for j in range(rect[1]+1, rect[3]):
                board[i][j] = 0
    
    q = deque()
    q.append((characterX, characterY, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0 ,1]
    
    while q:
        now = q.popleft()
        visited[now[0]][now[1]] = 1
        if now[0] == itemX and now[1] == itemY:
            answer = now[2]
            break
        else:
            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]
                if -1 < nx < 101 and -1 < ny < 101:
                    if board[nx][ny]:
                        if visited[nx][ny] == 0:
                            q.append((nx, ny, now[2]+1))
    return answer//2