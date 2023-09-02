def find_next_pos(board, loc):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    next_pos = []
    for i in range(4):
        nx = loc[0] + dx[i]
        ny = loc[1] + dy[i]
        if board[nx][ny] != 0:
            next_pos.append((nx,ny))
    return next_pos


def search(board, aloc, bloc, turn):
    if turn % 2 == 0:
        next_pos = find_next_pos(board, aloc)
    else:
        next_pos = find_next_pos(board, bloc)
    if len(next_pos) == 0:
        return turn % 2 != 0, turn
    if aloc == bloc:
        return turn % 2 == 0, turn + 1
    
    win, lose = [], []
    if turn % 2 == 0:
        board[aloc[0]][aloc[1]] = 0
        for nx, ny in next_pos:
            winner, cnt = search(board, [nx, ny], bloc, turn + 1)
            if winner:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[aloc[0]][aloc[1]] = 1
    else:
        board[bloc[0]][bloc[1]] = 0
        for nx, ny in next_pos:
            winner, cnt = search(board, aloc, [nx, ny], turn + 1)
            if not winner:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[bloc[0]][bloc[1]] = 1
    
    if win:
        return turn % 2 == 0, min(win)
    else:
        return turn % 2 != 0, max(lose)

def solution(board, aloc, bloc):
    new_board = [[0 for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[i+1][j+1] = board[i][j]
    for i in range(2):
        aloc[i] += 1
        bloc[i] += 1
    winner, answer = search(new_board, aloc, bloc, 0)
    return answer