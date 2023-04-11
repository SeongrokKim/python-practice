from collections import deque

def solution(n, computers):
    answer = 0
    i=0
    visit = [0]*len(computers)
    while i<n:
        if visit[i] == 0:
            d = deque()
            d.append(i)
            visit[i] = 1
            while d:
                k = d[0]
                for j in range(len(computers)):
                    if computers[k][j] == 1 and visit[j] == 0:
                        d.append(j)
                        visit[j] = 1
                
                d.popleft()
            answer += 1
        i += 1
        
    return answer