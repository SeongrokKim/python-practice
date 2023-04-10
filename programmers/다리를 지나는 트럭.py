from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    road = deque([])
    truck = deque(truck_weights)
    
    while True:
        road_sum = 0
        if not truck:
            if not road:
                break
        answer += 1
        
        if road:
            for i in range(len(road)):
                road[i][1] += 1
                road_sum += road[i][0]
            if road[0][1] >= bridge_length:
                road.popleft()
        if truck:
            if len(road) + 1 <= bridge_length and (road_sum + truck[0]) <= weight:
                t = truck.popleft()
                road.append([t,1])
    
    return answer +1