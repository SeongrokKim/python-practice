def solution(sequence):
    answer = 0
    newarr1 = []
    newarr2 = []
    table1 = []
    table2 = []
    answer = -1*float('inf')
    for i in range(len(sequence)):
        newarr1.append(sequence[i]*((-1)**i))
        newarr2.append(sequence[i]*((-1)**(i+1)))
        table1.append(sequence[i]*((-1)**i))
        table2.append(sequence[i]*((-1)**(i+1)))
    
    for i in range(len(newarr1)):
        if i >= 1:
            table1[i] = max(table1[i - 1] + newarr1[i], newarr1[i])
            table2[i] = max(table2[i - 1] + newarr2[i], newarr2[i])

    answer = max(answer, max(table1), max(table2))
    return answer
    