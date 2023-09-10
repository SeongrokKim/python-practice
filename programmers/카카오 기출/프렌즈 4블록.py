def solution(m, n, board):
    answer = 0
    table = [['' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            table[i][j] = board[i][j]
    while True:
        nothing = True
        remove_list = set()
        for i in range(m-1):
            for j in range(n-1):
                if table[i][j] != '-' and table[i][j] == table[i][j+1] and table[i][j+1] == table[i+1][j] and table[i+1][j] == table[i+1][j+1]:
                    nothing = False
                    remove_list.add((i, j))
                    remove_list.add((i, j+1))
                    remove_list.add((i+1, j))
                    remove_list.add((i+1, j+1))
        if nothing:
            break
        answer += len(remove_list)
        for x, y in remove_list:
            table[x][y] = "-"
        for i in range(n):
            j = 0
            while j < m - 1:
                if table[j+1][i] == '-' and table[j][i] != '-':
                    table[j+1][i] = table[j][i]
                    table[j][i] = '-'
                    j = -1
                j += 1
    return answer