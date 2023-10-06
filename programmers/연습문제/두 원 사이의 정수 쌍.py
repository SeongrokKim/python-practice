def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        if x < r1:
            l = (r1**2 - x**2)**0.5
            m = int((r2**2 - x**2)**0.5)
            if l-int(l) == 0:
                l = int(l)
            else:
                l = int(l) + 1
            answer += m-l+1
        else:
            answer += int((r2**2-x**2)**0.5)+1
    return answer*4