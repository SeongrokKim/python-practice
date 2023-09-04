def checkBo(board, x, y, w, n):
    if w:
        if 1 in board[x+1][y] or 1 in board[x+1][y+1] or (2 in board[x][y-1] and 2 in board[x][y+1]):
            board[x][y].append(2)
    else:
        if 2 in board[x][y-1]:
            if 1 not in board[x+1][y-1] and 1 not in board[x+1][y]:
                return
        if 2 in board[x][y+1]:
            if 1 not in board[x+1][y+1] and 1 not in board[x+1][y+2]:
                return
        if 1 in board[x][y]:
            if 1 not in board[x+1][y] and 2 not in board[x][y-1]:
                return
        if 1 in board[x][y+1]:
            if 1 not in board[x+1][y+1] and 2 not in board[x][y+1]:
                return
        board[x][y].remove(2)
        
def checkGi(board, x, y, w, n):
    if w:
        if x != n:
            if 2 not in board[x][y-1] and 2 not in board[x][y] and 1 not in board[x+1][y]:
                return
        board[x][y].append(1)
    else:
        if 2 in board[x-1][y-1]:
            if not((2 in board[x-1][y] and 2 in board[x-1][y-2]) or 1 in board[x][y-1]):
                return
        if 2 in board[x-1][y]:
            if not((2 in board[x-1][y-1] and 2 in board[x-1][y+1]) or 1 in board[x][y+1]):
                return
        if 1 in board[x-1][y]:
            if not(2 in board[x-1][y-1] or 2 in board[x-1][y]):
                return
        board[x][y].remove(1)

def solution(n, build_frame):
    answer = []
    board = [[[] for _ in range(n+1)] for _ in range(n+1)]
    for bf in build_frame:
        x = n-bf[1]
        y = bf[0]
        if bf[2]:
            checkBo(board, x, y, bf[3], n)
        else:
            checkGi(board, x, y, bf[3], n)
    for j in range(n+1):
        for i in range(n, -1, -1):
            if 1 in board[i][j]:
                answer.append([j, n-i, 0])
            if 2 in board[i][j]:
                answer.append([j, n-i, 1])
    return answer