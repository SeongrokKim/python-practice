def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[0]))
    end = targets[0][1]
    for s, e in targets:
        if s < end:
            if e < end:
                end = e
        else:
            answer += 1
            end = e
    answer += 1
    return answer