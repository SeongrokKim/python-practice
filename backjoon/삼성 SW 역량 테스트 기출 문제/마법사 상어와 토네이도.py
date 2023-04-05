n=int(input())
A=[]
tot=0

for i in range (n):
    A.append(list(map(int, input().split())))
    for j in range(n):
        tot += A[i][j]

dy=[-1, 0, 1, 0]
dx=[0, 1, 0, -1]
x = n//2
y = n//2

leng = 1

step = 0
way = 0

def move(way, x, y):
    firstSand=A[x][y]
    per5= int(firstSand*0.05)
    per10= int(firstSand*0.1)
    per7= int(firstSand*0.07)
    per2= int(firstSand*0.02)
    per1= int(firstSand*0.01)

    if x+dx[way%4]+dx[(way+1)%4] > -1 and y+dy[way%4]+dy[(way+1)%4] > -1 and x+dx[way%4]+dx[(way+1)%4] < n and y+dy[way%4]+dy[(way+1)%4] < n:
        A[x+dx[way%4]+dx[(way+1)%4]][y+dy[way%4]+dy[(way+1)%4]] += per10
    
    if x+dx[way%4]+dx[(way+3)%4] > -1 and y+dy[way%4]+dy[(way+3)%4] > -1 and x+dx[way%4]+dx[(way+3)%4] < n and y+dy[way%4]+dy[(way+3)%4] < n:
        A[x+dx[way%4]+dx[(way+3)%4]][y+dy[way%4]+dy[(way+3)%4]] += per10
    
    if x+dx[(way+1)%4] > -1 and y+dy[(way+1)%4] > -1 and x+dx[(way+1)%4] < n and y+dy[(way+1)%4] < n:
        A[x+dx[(way+1)%4]][y+dy[(way+1)%4]] += per7
    
    if x+dx[(way+3)%4] > -1 and y+dy[(way+3)%4] > -1 and x+dx[(way+3)%4] < n and y+dy[(way+3)%4] < n:
        A[x+dx[(way+3)%4]][y+dy[(way+3)%4]] += per7
    
    if x+dx[(way+2)%4]+dx[(way+1)%4] > -1 and y+dy[(way+2)%4]+dy[(way+1)%4] > -1 and x+dx[(way+2)%4]+dx[(way+1)%4] < n and y+dy[(way+2)%4]+dy[(way+1)%4] < n:
        A[x+dx[(way+2)%4]+dx[(way+1)%4]][y+dy[(way+2)%4]+dy[(way+1)%4]] += per1
    
    if x+dx[(way+2)%4]+dx[(way+3)%4] > -1 and y+dy[(way+2)%4]+dy[(way+3)%4] > -1 and x+dx[(way+2)%4]+dx[(way+3)%4] < n and y+dy[(way+2)%4]+dy[(way+3)%4] < n:
        A[x+dx[(way+2)%4]+dx[(way+3)%4]][y+dy[(way+2)%4]+dy[(way+3)%4]] += per1
    
    if x+dx[way%4] > -1 and y+dy[way%4] > -1 and x+dx[way%4] < n and y+dy[way%4] < n:
        A[x+dx[way%4]][y+dy[way%4]] += (firstSand - (per5 + 2*(per10 + per7 + per2 + per1)))

    if x+dx[(way)%4]*2 > -1 and y+dy[(way)%4]*2 > -1 and x+dx[(way)%4]*2 < n and y+dy[(way)%4]*2 < n:
        A[x+dx[(way)%4]*2][y+dy[(way)%4]*2] += per5

    if x+dx[(way+1)%4]*2 > -1 and y+dy[(way+1)%4]*2 > -1 and x+dx[(way+1)%4]*2 < n and y+dy[(way+1)%4]*2 < n:
        A[x+dx[(way+1)%4]*2][y+dy[(way+1)%4]*2] += per2

    if x+dx[(way+3)%4]*2 > -1 and y+dy[(way+3)%4]*2 > -1 and x+dx[(way+3)%4]*2 < n and y+dy[(way+3)%4]*2 < n:
        A[x+dx[(way+3)%4]*2][y+dy[(way+3)%4]*2] += per2
    
    A[x][y] = 0

    

while(not (x==0 and y ==0)):
    for i in range(leng):
        x+=dx[way%4]
        y+=dy[way%4]
        move(way, x, y)
        if x==0 and y==0:
            break
    if step == 1:
        leng += 1
        step = 0
    else:
        step += 1
    way += 1

rest = 0
for i in range(n):
    for j in range(n):
        rest += A[i][j]
out = tot - int(rest)
print(out)