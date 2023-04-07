from collections import deque
n,q= map(int,input().split())
size = 2**n
link = []
for i in range(size):
    link.append(list(map(int,input().split())))

l=list(map(int,input().split()))

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def fireStorm(l):
    # 격자 나누기
    # 격자 돌리기
    r=0
    c=0
    newLink = [[0 for _ in range(size)] for _ in range(size)]
    for k in range(0,size,2**l):
        for m in range(0, size, 2**l):
            for i in range(2**l):
                for j in range(2**l):
                    newLink[k+i][m+j]=link[k+2**l-1-j][m+i]

    # 얼음 3개 이상 인접 x -= 1
    finalLink = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if newLink[i][j] == 0:
                finalLink[i][j] = 0
            else:
                cnt = 0
                if j+dy[0]>-1 and newLink[i+dx[0]][j+dy[0]] != 0:
                    cnt += 1
                if i+dx[1]>-1 and newLink[i+dx[1]][j+dy[1]] != 0:
                    cnt += 1
                if j+dy[2]<size and newLink[i+dx[2]][j+dy[2]] != 0:
                    cnt += 1
                if i+dx[3]<size and newLink[i+dx[3]][j+dy[3]] != 0:
                    cnt += 1
                if cnt>=3:
                    finalLink[i][j] = newLink[i][j]
                else:
                    finalLink[i][j] = newLink[i][j] - 1
    
    for i in range(size):
        for j in range(size):
            link[i][j] = finalLink[i][j]

for i in range(q):
    fireStorm(l[i])

tot = 0
for i in range(size):
    for j in range(size):
        tot += link[i][j]

visited = [[False for _ in range(size)] for _ in range(size)]

q=deque()
big = 0

def bfs(i,j):
    cnt = 0
    q.append([i,j])
    visited[i][j] = True
    while len(q)>0:
        now = q.popleft()
        cnt += 1

        if now[1]+dy[0]>-1 and link[now[0]+dx[0]][now[1]+dy[0]] != 0 and visited[now[0]+dx[0]][now[1]+dy[0]] == False:
            q.append([now[0]+dx[0],now[1]+dy[0]])
            visited[now[0]+dx[0]][now[1]+dy[0]] = True
        if now[0]+dx[1]>-1 and link[now[0]+dx[1]][now[1]+dy[1]] != 0 and visited[now[0]+dx[1]][now[1]+dy[1]] == False:
            q.append([now[0]+dx[1],now[1]+dy[1]])
            visited[now[0]+dx[1]][now[1]+dy[1]] = True
        if now[1]+dy[2]<size and link[now[0]+dx[2]][now[1]+dy[2]] != 0 and visited[now[0]+dx[2]][now[1]+dy[2]] == False:
            q.append([now[0]+dx[2],now[1]+dy[2]])
            visited[now[0]+dx[2]][now[1]+dy[2]] = True
        if now[0]+dx[3]<size and link[now[0]+dx[3]][now[1]+dy[3]] != 0 and visited[now[0]+dx[3]][now[1]+dy[3]] == False:
            q.append([now[0]+dx[3],now[1]+dy[3]])
            visited[now[0]+dx[3]][now[1]+dy[3]] = True

    return cnt

for i in range(size):
    for j in range(size):
        if not visited[i][j] and link[i][j] != 0:
            tmp = bfs(i,j)
            big = max(big, tmp)

print(tot)
print(big)