def solution(n, s):
    answer = []
    if n>s:
        return [-1]
    
    q = s // n
    r = s % n
    for i in range(n-r):
        answer.append(q)
    for i in range(r):
        answer.append(q+1)
    return answer