def solution(id_list, report, k):
    answer = [0] * len(id_list)
    rep_dict = {id: [] for id in id_list}
    report=list(set(report))
    
    for r in report:
        s=r.split()
        rep_dict[s[1]].append(s[0])
        
    for m,n in rep_dict.items():
        if len(n) >= k:
            for reporter in n:
                answer[id_list.index(reporter)] += 1
            
    return answer