n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
answer = 0

way = [[0,1],[-1,0],[0,-1],[1,0]]


def curve(x, y, d, g, board):
    board[x][y] = 1
    board[x+way[d][0]][y+way[d][1]] = 1
    dragon = [[x,y],[x+way[d][0],y+way[d][1]]]
    if g == 0:
        return
    else:
        cnt = 0
        while cnt<g:
            tail = len(dragon)-1
            for i in range(tail-1,-1,-1):
                dx = dragon[tail][0] - dragon[i][0]
                dy = dragon[tail][1] - dragon[i][1]
                nx = dragon[i][0]
                ny = dragon[i][1]
                if dx>0:
                    while dx>0:
                        nx += 1
                        ny += 1
                        dx -= 1
                elif dx<0:
                    while dx<0:
                        nx -= 1
                        ny -= 1
                        dx += 1
                if dy>0:
                    while dy>0:
                        nx -= 1
                        ny += 1
                        dy -= 1
                elif dy<0:
                    while dy<0:
                        nx += 1
                        ny -= 1
                        dy += 1
                board[nx][ny] = 1
                dragon.append([nx,ny])
            cnt += 1


for i in range(n):
    x,y,d,g=map(int, input().split())
    curve(y,x,d,g,board)

for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
            answer += 1

print(answer)