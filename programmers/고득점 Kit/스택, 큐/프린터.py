from collections import deque
def solution(priorities, location):
    answer = 0
    prideq = deque()
    idxdeq = deque()
    for p in priorities:
        prideq.append(p)
    for i in range(len(priorities)):
        idxdeq.append(i)
    while location in idxdeq:
        first = max(priorities)
        if first == prideq[0]:
            priorities.remove(first)
            prideq.popleft()
            idxdeq.popleft()
            answer += 1
        else:
            prideq.rotate(-1)
            idxdeq.rotate(-1)
    return answer