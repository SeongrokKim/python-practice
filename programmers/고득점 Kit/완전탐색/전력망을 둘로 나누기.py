def find(x, parent):
    if x!=parent[x]:
        x = parent[x]
        return find(x,parent)
    return x

def union(x, y, parent):
    xp = find(x, parent)
    yp = find(y, parent)
    
    if xp<yp:
        parent[yp] = xp
    else:
        parent[xp] = yp


def solution(n, wires):
    answer = n
    for w in wires:
        parent = []
        for i in range(n):
            parent.append(i)
        tmp = wires[:][:]
        tmp.remove(w)
        for x, y in tmp:
            union(x-1, y-1, parent)
        
        for x,y in wires:
            parent[x-1] = find(x-1, parent)
            parent[y-1] = find(y-1, parent)
        setParent = set(parent)
        cnt = []
        for s in setParent:
            cnt.append(parent.count(s))
        answer = min(answer, max(cnt)-min(cnt))
    return answer