def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x:x[2])
    parent = [i for i in range(n)]
    def find(x):
        if x != parent[x]:
            x = parent[x]
            return find(x)
        return x
    def union(x, y):
        xp = find(x)
        yp = find(y)
        if xp<yp:
            parent[yp] = xp
        elif yp<xp:
            parent[xp] = yp
    bridge= 0
    for line in costs:
        if find(line[0]) != find(line[1]):
            union(line[0], line[1])
            bridge += 1
            answer += line[2]
        if bridge == n-1:
            break
    return answer