from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        pos = limit
        boat = []
        fat = people.pop()
        boat.append(fat)
        answer += 1
        if people:
            if fat <= limit//2:
                people.pop()
            else:
                pos -= fat
                if people[0]<=pos:
                    people.popleft()
    return answer