def solution(places):
    answer = []
    for place in places:
        ps = []
        xs = []
        can = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    ps.append([i,j])
                if place[i][j] == 'X':
                    xs.append([i,j])
        for i in range(len(ps) -1):
            for j in range(i+1,len(ps)):
                if (abs(ps[i][0]-ps[j][0]) + abs(ps[i][1]-ps[j][1])) == 1:
                    can = 0
                elif (abs(ps[i][0]-ps[j][0]) + abs(ps[i][1]-ps[j][1])) == 2:
                    if ps[i][0] == ps[j][0]:
                        if [ps[i][0], (ps[i][1]+ps[j][1])/2] not in xs:
                            can = 0
                            break
                    elif ps[i][1] == ps[j][1]:
                        if [(ps[i][0]+ps[j][0])/2, ps[i][1]] not in xs:
                            can = 0
                            break
                    else:
                        if [ps[i][0], ps[j][1]] not in xs or [ps[j][0], ps[i][1]] not in xs:
                            can = 0
                            break
                            
        
        answer.append(can)
    return answer