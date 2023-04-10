def solution(record):
    answer = []
    user = dict()
    action = []
    for r in record:
        info = r.split()
        if info[0] == "Enter" or info[0] == "Change":
            user[info[1]] = info[2]
        action.append((info[0], info[1]))
                    
    for a in action:
        if a[0] == "Enter":
            answer.append(f'{user[a[1]]}님이 들어왔습니다.')
        elif a[0] == "Leave":
            answer.append(f'{user[a[1]]}님이 나갔습니다.')
    return answer