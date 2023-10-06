from collections import defaultdict, deque
def solution(n, edge):
    answer = 0
    edges = defaultdict(list)
    visited = [0 for _ in range(n+1)]
    for s, e in edge:
        edges[s].append(e)
        edges[e].append(s)
    q = deque()
    maxd = 0
    q.append((1, 0))
    while q:
        now = q.popleft()
        if visited[now[0]]:
            continue
        else:
            visited[now[0]] = 1
            if now[1]>maxd:
                answer = 0
                maxd = now[1]
            answer += 1
            for node in edges[now[0]]:
                q.append((node, now[1]+1))
    return answer