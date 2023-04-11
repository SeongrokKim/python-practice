def solution(n, works):
    answer = 0
    tot = 0
    for w in works:
        tot += w
    if tot < n :
        return 0
    works.sort()
    works.reverse()
    while n > 0:
        cnt = 1
        i = 0
        while works[i] == works[i+1]:
            i += 1
            cnt += 1
            if i == len(works) - 1:
                break
        if n > cnt:
            for i in range(cnt):
                works[i] -= 1
            n -= cnt
        else:
            for i in range(n):
                works[i] -= 1
            break
    
    for w in works:
        answer += w*w
    return answer