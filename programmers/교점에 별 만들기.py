def solution(line):
    spot = []
    for i in range(len(line)-1):
        for j in range(i, len(line)):
            if (line[i][0]*line[j][1]-line[i][1]*line[j][0]):
                x=(line[j][2]*line[i][1]-line[i][2]*line[j][1])/(line[i][0]*line[j][1]-line[i][1]*line[j][0])
                y=(line[i][0]*line[j][2]-line[j][0]*line[i][2])/(line[j][0]*line[i][1]-line[i][0]*line[j][1])
                spot.append([x, y])
    r_spot = []
    for s in spot:
        if int(s[0]) == s[0] and int(s[1]) == s[1]:
            if [int(s[0]), int(s[1])] not in r_spot:
                r_spot.append([int(s[0]), int(s[1])])
    INF = float('inf')
    maxr= -INF
    maxc= -INF
    minr= INF
    minc= INF
    for m in r_spot:
        maxr = max(maxr, m[1])
        maxc = max(maxc, m[0])
        minr = min(minr, m[1])
        minc = min(minc, m[0])
    r = maxr - minr + 1
    c = maxc - minc + 1
    res = [['.' for _ in range(c)] for _ in range(r)]
    for x,y in r_spot:
        res[maxr-y][x-minc] = '*'
    answer = [''.join(s) for s in res]
          
    return answer
