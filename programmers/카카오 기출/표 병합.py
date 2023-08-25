def solution(commands):
    answer = []
    cell = [['' for _ in range(51)] for _ in range(51)]
    group = []
    for i in range(1, 51):
        for j in range(1, 51):
            group.append([(i, j)])
    
    for command in commands:
        comm =list(map(str,command.split()))
        com = comm[0]
        if com == 'UPDATE':
            if len(comm) == 4:
                r = comm[1]
                c = comm[2]
                val = comm[3]
                for g in group:
                    if (int(r), int(c)) in g:
                        for i in g:
                            cell[i[0]][i[1]] = val
            else:
                val1 = comm[1]
                val2 = comm[2]
                for i in range(51):
                    for j in range(51):
                        if cell[i][j] == val1:
                            cell[i][j] = val2
        elif com == 'MERGE':
            r1 = int(comm[1])
            c1 = int(comm[2])
            r2 = int(comm[3])
            c2 = int(comm[4])
            if r1 != r2 or c1 != c2:
                m1 = []
                m2 = []
                for g in group:
                    if len(m1) == 0:
                        if (r1, c1) in g:
                            m1 = g
                    if len(m2) == 0:
                        if (r2, c2) in g:
                            m2 = g
                if m1 == m2:
                    continue
                if cell[m1[0][0]][m1[0][1]] == '':
                    if cell[m2[0][0]][m2[0][1]] != '':
                        for m in m1:
                            cell[m[0]][m[1]] = cell[m2[0][0]][m2[0][1]]
                else:
                    for m in m2:
                        cell[m[0]][m[1]] = cell[m1[0][0]][m1[0][1]]
                m1 += m2
                group.remove(m2)
        elif com == 'UNMERGE':
            r = int(comm[1])
            c = int(comm[2])
            tar = []
            for g in group:
                if (r, c) in g:
                    tar = g
                    break
            for t in tar:
                if t != (r, c):
                    cell[t[0]][t[1]] = ''
                group.append([(t[0], t[1])])
            group.remove(tar)
        elif com == 'PRINT':
            r = comm[1]
            c = comm[2]
            if cell[int(r)][int(c)] == '':
                answer.append('EMPTY')
            else:
                answer.append(cell[int(r)][int(c)])
    return answer