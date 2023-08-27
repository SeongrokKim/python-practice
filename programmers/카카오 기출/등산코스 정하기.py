from collections import defaultdict
from collections import deque
import heapq
def solution(n, paths, gates, summits):
    answer = []
    intensity = [int(1e9) for _ in range(n + 1)]
    route = defaultdict(list)
    for path in paths:
        route[path[0]].append((path[2], path[1]))
        route[path[1]].append((path[2], path[0]))
    
    visited = [0 for _ in range(n+1)]
    q = deque()
    h = []
    for gate in gates:
        visited[gate] = 1
        intensity[gate] = 0
    for gate in gates:
        for can in route[gate]:
            if visited[can[1]] == 0:
                heapq.heappush(h, can)
                intensity[can[1]] = min(intensity[can[1]], can[0])
    hp = heapq.heappop(h)
    q.append(hp[1])
    while q:
        now = q.popleft()
        if now in summits:
            answer.append((now, intensity[now]))
        else:
            visited[now] = 1
            for can in route[now]:
                if intensity[can[1]] > max(intensity[now], can[0]):
                    heapq.heappush(h, (max(intensity[now], can[0]), can[1]))
                    intensity[can[1]] = max(intensity[now], can[0])
        while h:
            hp = heapq.heappop(h)
            if answer:
                if hp[0] > answer[0][1]:
                    continue
            if hp[1] not in q:
                q.append(hp[1])
            if h:
                if h[0][0] == hp[0]:
                    pass
                else:
                    break
    minimum = [int(1e9), int(1e9)]
    for i in range(len(intensity)):
        if i in summits:
            if intensity[i] < minimum[1]:
                minimum = [i, intensity[i]]
    return minimum