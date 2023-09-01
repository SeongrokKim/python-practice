def solution(board, skill):
    answer = 0
    
    def attack(board, r1, c1, r2, c2, degree):
        board[r1][c1] -= degree
        board[r1][c2+1] += degree
        board[r2+1][c1] += degree
        board[r2+1][c2+1] -= degree
    
    def recover(board, r1, c1, r2, c2, degree):
        board[r1][c1] += degree
        board[r1][c2+1] -= degree
        board[r2+1][c1] -= degree
        board[r2+1][c2+1] += degree
    
    new_board = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for s in skill:
        if s[0] == 1:
            attack(new_board, s[1], s[2], s[3], s[4], s[5])
        else:
            recover(new_board, s[1], s[2], s[3], s[4], s[5])
    
    for i in range(len(new_board)):
        for j in range(len(new_board[0])-1):
            new_board[i][j+1] += new_board[i][j]
            
    for j in range(len(new_board[0])):
        for i in range(len(new_board)-1):
            new_board[i+1][j] += new_board[i][j]
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] + new_board[r][c] > 0:
                answer += 1
    
    return answer