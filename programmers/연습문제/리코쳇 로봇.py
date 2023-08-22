from collections import deque
def solution(board):
    answer = -1
    rowSize = len(board)
    colSize = len(board[0])
    newBoard = [[0 for _ in range(colSize)] for _ in range(rowSize)]
    dList = []
    start = goal = (-1,-1)
    for i in range(rowSize):
        for j in range(colSize):
            if board[i][j] == 'D':
                newBoard[i][j] = -1
                dList.append((i,j))
            elif board[i][j] == 'R':
                newBoard[i][j] = 1
                start = (i,j)
            if board[i][j] == 'G':
                newBoard[i][j] = 2
                goal = (i,j)
    
    visited = [[-1 for _ in range(colSize)] for _ in range(rowSize)]
    visited[start[0]][start[1]] = 1
    q = deque()
    q.appendleft((start[0],start[1],0))
    cnt = 1
    while q:
        now = q.pop()
        nowX = now[0]
        nowY = now[1]
        nowCost = now[2]
        if (nowX, nowY) == goal:
            answer = nowCost
            break
        else:
            cand = []
            if nowY > 0:
                while nowY > -1:
                    if nowY == 0:
                        cand.append((nowX, 0))
                        break
                    else:
                        nowY -= 1
                        if (nowX, nowY) in dList:
                            cand.append((nowX, nowY+1))
                            break
            nowY = now[1]
            if nowY < colSize - 1:
                while nowY < colSize:
                    if nowY == colSize - 1:
                        cand.append((nowX, colSize-1))
                        break
                    else:
                        nowY += 1
                        if (nowX, nowY) in dList:
                            cand.append((nowX, nowY-1))
                            break
            nowY = now[1]
            if nowX > 0:
                while nowX > -1:
                    if nowX == 0:
                        cand.append((0, nowY))
                        break
                    else:
                        nowX -= 1
                        if (nowX, nowY) in dList:
                            cand.append((nowX+1, nowY))
                            break
            nowX = now[0]
            if nowX < rowSize - 1:
                while nowX < rowSize:
                    if nowX == rowSize - 1:
                        cand.append((rowSize-1, nowY))
                        break
                    else:
                        nowX += 1
                        if (nowX, nowY) in dList:
                            cand.append((nowX-1, nowY))
                            break
            nowX = now[0]
            
            for c in cand:
                if visited[c[0]][c[1]] == -1:
                    visited[c[0]][c[1]] = 1
                    q.appendleft((c[0],c[1],nowCost+1))
    
    return answer