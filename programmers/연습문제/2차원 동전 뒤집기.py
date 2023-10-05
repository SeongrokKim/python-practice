def solution(beginning, target):
    answer = [int(1e9), int(1e9), int(1e9), int(1e9)]
    find = [0, 0, 0, 0]
    
    board = [[1 for _ in range(len(beginning[0]))] for _ in range(len(beginning))]
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if beginning[i][j] == target[i][j]:
                board[i][j] = 0
    for j in range(len(beginning)):
        if board[j][0] == 1:
            for i in range(len(beginning[0])):
                if board[j][i] == 0:
                    board[j][i] = 1
                else:
                    board[j][i] = 0
            answer[0] += 1
    for i in range(len(beginning[0])):
        if board[0][i] == 1:
            for j in range(len(beginning)):
                if board[j][i] == 0:
                    board[j][i] = 1
                else:
                    board[j][i] = 0
            answer[0] += 1
    fail = False
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if board[i][j] == 1:
                fail = True
                break
        if fail:
            break
    if fail == False:
        find[0] = 1
        answer[0] -= int(1e9)
    
    board = [[1 for _ in range(len(beginning[0]))] for _ in range(len(beginning))]
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if beginning[i][j] == target[i][j]:
                board[i][j] = 0
    
    for j in range(len(beginning[0])):
        if board[0][j] == 1:
            for i in range(len(beginning)):
                if board[i][j] == 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            answer[1] += 1
    for i in range(len(beginning)):
        if board[i][0] == 1:
            for j in range(len(beginning[0])):
                if board[i][j] == 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            answer[1] += 1
    fail = False
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if board[i][j] == 1:
                fail = True
                break
        if fail:
            break
    if fail == False:
        find[1] = 1
        answer[1] -= int(1e9)
    
    board = [[1 for _ in range(len(beginning[0]))] for _ in range(len(beginning))]
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if beginning[i][j] == target[i][j]:
                board[i][j] = 0
    for j in range(len(beginning)):
        if board[j][0] == 0:
            for i in range(len(beginning[0])):
                if board[j][i] == 0:
                    board[j][i] = 1
                else:
                    board[j][i] = 0
            answer[2] += 1
    for i in range(len(beginning[0])):
        if board[0][i] == 1:
            for j in range(len(beginning)):
                if board[j][i] == 0:
                    board[j][i] = 1
                else:
                    board[j][i] = 0
            answer[2] += 1
    fail = False
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if board[i][j] == 1:
                fail = True
                break
        if fail:
            break
    if fail == False:
        find[2] = 1
        answer[2] -= int(1e9)
    
    board = [[1 for _ in range(len(beginning[0]))] for _ in range(len(beginning))]
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if beginning[i][j] == target[i][j]:
                board[i][j] = 0
    
    for j in range(len(beginning[0])):
        if board[0][j] == 0:
            for i in range(len(beginning)):
                if board[i][j] == 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            answer[3] += 1
    for i in range(len(beginning)):
        if board[i][0] == 1:
            for j in range(len(beginning[0])):
                if board[i][j] == 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            answer[3] += 1
    fail = False
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if board[i][j] == 1:
                fail = True
                break
        if fail:
            break
    if fail == False:
        find[3] = 1
        answer[3] -= int(1e9)
        
    if 1 in find:
        return min(answer)
    else:
        return -1