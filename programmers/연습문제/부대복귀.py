from collections import defaultdict, deque
def solution(n, roads, sources, destination):
    answer = []
    dist = [int(1e9) for _ in range(n+1)]
    dist[destination] = 0
    road_info = defaultdict(list)
    for road in roads:
        road_info[road[0]].append(road[1])
        road_info[road[1]].append(road[0])
    q = deque()
    q.append((destination, 0))
    while q:
        now, cost = q.popleft()
        for r in road_info[now]:
            if dist[r] > dist[now]+1:
                q.append((r, cost+1))
                dist[r] = cost + 1
    
    for source in sources:
        if dist[source] == int(1e9):
            answer.append(-1)
        else:
            answer.append(dist[source])
    return answer