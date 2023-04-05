n=int(input())
stuNum = n*n
stuSeq = []
stuLove = []
temp = []
classRoom = [[0 for _ in range(n)] for _ in range(n)]
for i in range(stuNum):
    temp.append(list(map(int,input().split())))
    stuSeq.append(temp[i][0])
    stuLove.append(temp[i][1:])


    
dy=[-1, 0, 1, 0]
dx=[0, 1, 0, -1]

def numLover(i, j, k):
    num = 0
    for l in range(4):
        nj = j + dy[l]
        nk = k + dx[l]
        if nj > -1 and nk > -1 and nj < n and nk < n:
            if classRoom[nj][nk] in stuLove[i]:
                num += 1
    return [num, j, k]

def findZero(x, y):
    num = 0
    for l in range(4):
        ny = y + dy[l]
        nx = x + dx[l]
        if ny > -1 and nx > -1 and ny < n and nx < n:
            if classRoom[nx][ny] == 0:
                num += 1
    return [num, x, y]

for i in range(stuNum):
    if i == 0:
        classRoom[1][1] = stuSeq[0]
    else:
        loveNum = []        
        condition1 = []
        zeroNum = []
        condition2 = []
        for j in range(n):
            for k in range(n):
                if classRoom[j][k] == 0:
                    loveNum.append(numLover(i, j, k))
        maximum = 0
        for j in range(len(loveNum)):
            if loveNum[j][0] > maximum:
                maximum = loveNum[j][0]
        for j in range(len(loveNum)):
            if loveNum[j][0] == maximum:
                condition1.append(loveNum[j])
        for j in range(len(condition1)):
            zeroNum.append(findZero(condition1[j][1], condition1[j][2]))
        maxzero = 0
        for j in range(len(zeroNum)):
            if zeroNum[j][0]>maxzero:
                maxzero=zeroNum[j][0]
        for j in range(len(zeroNum)):
            if zeroNum[j][0]==maxzero:
                condition2.append(zeroNum[j])
        classRoom[condition2[0][1]][condition2[0][2]] = stuSeq[i]


def calGood(i):
    friend = 0
    stu = stuSeq[i]
    for l in range(n):
        for m in range(n):
            if classRoom[l][m] == stu:
                for o in range(4):
                    nl = l + dx[o]
                    nm = m + dy[o]
                    if nl>-1 and nm>-1 and nl<n and nm<n:
                        if classRoom[nl][nm] in stuLove[i]:
                            friend += 1
    if friend == 1:
        return 1
    elif friend == 2:
        return 10
    elif friend == 3:
        return 100
    elif friend == 4:
        return 1000
    return 0

good = 0
for i in range(stuNum):
    good += calGood(i)
print(good)