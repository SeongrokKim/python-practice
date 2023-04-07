r,c,t = map(int, input().split())

room = []
for i in range(r):
    tmp = list(map(int,input().split()))
    room.append(tmp)

for i in range(r):
    if room[i][0] == -1:
        gc1 = i
        gc2 = i+1
        break

def diffusion():
    newRoom = [[0 for _ in range(c)] for _ in range(r)]
    newRoom[gc1][0] = -1
    newRoom[gc2][0] = -1
    for i in range(r):
        for j in range(c):
            difNum = 0
            if room[i][j] == -1 or room[i][j] == 0:
                continue
            if j-1>-1 and room[i][j-1] != -1:
                newRoom[i][j-1] += room[i][j]//5
                difNum += 1
            if i-1>-1 and room[i-1][j] != -1:
                newRoom[i-1][j] += room[i][j]//5
                difNum += 1
            if j+1<c:
                newRoom[i][j+1] += room[i][j]//5
                difNum += 1
            if i+1<r and room[i+1][j] != -1:
                newRoom[i+1][j] += room[i][j]//5
                difNum += 1
            room[i][j] -= (room[i][j]//5 * difNum)
            newRoom[i][j] += room[i][j]
    for i in range(r):
        for j in range(c):
            room[i][j]=newRoom[i][j]

def upOperation():
    for i in range(gc1-2,-1,-1):
        room[i+1][0] = room[i][0]
    for i in range(1,c):
        room[0][i-1] = room[0][i]
    for i in range(1,gc1+1):
        room[i-1][c-1] = room[i][c-1]
    for i in range(c-2,0,-1):
        room[gc1][i+1] = room[gc1][i]
    room[gc1][1] = 0

def downOperation():
    for i in range(gc2+2,r):
        room[i-1][0] = room[i][0]
    for i in range(1,c):
        room[r-1][i-1] = room[r-1][i]
    for i in range(r-2,gc2-1,-1):
        room[i+1][c-1] = room[i][c-1]
    for i in range(c-2,0,-1):
        room[gc2][i+1] = room[gc2][i]
    room[gc2][1] = 0
cnt = 0
while cnt<t:
    diffusion()
    upOperation()
    downOperation()
    cnt += 1

answer = 0
for i in range(r):
    for j in range(c):
        answer += room[i][j]

print(answer+2)
