from collections import deque

t = int(input())
for i in range(t):
    answer = 0
    n, m= map(int, input().split())
    p = deque(list(map(int, input().split())))
    idx = deque()
    for j in range(n):
        idx.append(j)
    while m in idx:
        first = max(p)
        if first == p[0]:
            p.popleft()
            idx.popleft()
            answer += 1
        else:
            p.rotate(-1)
            idx.rotate(-1)
    print(answer)