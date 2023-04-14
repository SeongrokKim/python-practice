def solution(name):
    answer = 0
    
    shift = len(name)-1
    
    for i, n in enumerate(name):
        answer += min(ord(n) - ord('A'), ord('Z')-ord(n) + 1)
        
        nxt = i+1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1
        
        shift = min([shift, 2*i + len(name) - nxt, i + 2*(len(name)-nxt)])
    return answer + shift