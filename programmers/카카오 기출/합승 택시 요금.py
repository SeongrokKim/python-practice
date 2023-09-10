# 플로이드 워셜
# def solution(n, s, a, b, fares):
#     answer = int(1e9)
#     fare_info = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]
#     for i in range(n+1):
#         fare_info[i][i] = 0
#     for fare in fares:
#         fare_info[fare[0]][fare[1]] = fare[2]
#         fare_info[fare[1]][fare[0]] = fare[2]
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             for k in range(1, n+1):
#                 fare_info[j][k] = min(fare_info[j][k], fare_info[j][i] + fare_info[i][k])

#     for i in range(1, n+1):
#         answer = min(answer, fare_info[i][s]+fare_info[i][a]+fare_info[i][b])
#     return answer

# 다익스트라
from collections import defaultdict
import heapq
def solution(n, s, a, b, fares):
    answer = int(1e9)
    fare_info = defaultdict(list)
    for fare in fares:
        fare_info[fare[0]].append((fare[2], fare[1]))
        fare_info[fare[1]].append((fare[2], fare[0]))
    table1 = [int(1e9) for _ in range(n+1)]
    table1[s] = 0
    q = []
    q.append((0, s))
    while q:
        now = heapq.heappop(q)
        for edge, node in fare_info[now[1]]:
            if table1[node] > table1[now[1]] + edge:
                table1[node] = table1[now[1]] + edge
                heapq.heappush(q, (edge, node))
    
    table2 = [int(1e9) for _ in range(n+1)]
    table2[a] = 0
    q = []
    q.append((0, a))
    while q:
        now = heapq.heappop(q)
        for edge, node in fare_info[now[1]]:
            if table2[node] > table2[now[1]] + edge:
                table2[node] = table2[now[1]] + edge
                heapq.heappush(q, (edge, node))
    
    table3 = [int(1e9) for _ in range(n+1)]
    table3[b] = 0
    q = []
    q.append((0, b))
    while q:
        now = heapq.heappop(q)
        for edge, node in fare_info[now[1]]:
            if table3[node] > table3[now[1]] + edge:
                table3[node] = table3[now[1]] + edge
                heapq.heappush(q, (edge, node))
                
    for i in range(1, n+1):
        answer = min(answer, table1[i] + table2[i] + table3[i])
    return answer
