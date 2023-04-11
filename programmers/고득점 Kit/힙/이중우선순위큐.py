def solution(operations):
    answer = []
    for op in operations:
        op=op.split()
        if op[0] == 'I':
            answer.append(int(op[1]))
        else:
            if len(answer):
                if op[1] == '1':
                    answer.remove(max(answer))
                       
                else:
                    answer.remove(min(answer))
    
    if len(answer):
        return [max(answer), min(answer)]
    else:
        return [0, 0]