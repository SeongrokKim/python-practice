from collections import deque

def solution(s):
    answer = True
    d= deque()
    for i in range(len(s)):
        if s[i] == '(':
            d.append(s[i])
        else:
            if d:
                d.pop()
            else:
                return False
    if d:
        return False

    return True