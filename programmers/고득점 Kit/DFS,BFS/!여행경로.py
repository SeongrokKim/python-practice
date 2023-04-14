from collections import defaultdict
def solution(tickets):
    answer = []
    ticket = defaultdict(list)
    for tick in tickets:
        ticket[tick[0]].append(tick[1])
    
    for t in ticket.keys():
        ticket[t].sort(reverse=True)
    
    num = len(tickets)
    def dfs(ticket, num, answer, f):
        answer.append(f)
        if len(answer) == num+1:
            return True
        if f not in ticket:
            answer.pop()
            return False
        for i in range(len(ticket[f])):
            to = ticket[f][-1]
            ticket[f].pop()
            
            if dfs(ticket, num, answer, to):
                return True
            ticket[f].insert(0, to)
        
        answer.pop()
        return False
    
    
    if dfs(ticket, num, answer, "ICN"):
        return answer
    
    return answer
        
