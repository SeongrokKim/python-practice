n, k = map(int, input().split())
con = list(map(int, input().split()))
leng = len(con)
rob = [0] * n

level = 1

def rotate():
    temp1 = con[leng-1]
    con[1:] = con[:leng-1]
    rob[1:] = rob[:n-1]
    con[0] = temp1
    rob[0] = 0
    if(rob[n-1]):
        rob[n-1]=0

def check(idx:int):
    if rob[idx+1] == 0 and con[idx+1] > 0:
        return True
    return False

def move():
    for i in range(n-2):
        if (rob[n-2-i]):
            idx = n-2-i
            if (check(idx)):
                con[idx+1] -= 1
                rob[idx+1] = rob[idx]
                rob[idx] = 0
                
    if(rob[n-1]):
        rob[n-1]=0

while (True):
    rotate()
    move()
    if con[0]>0 and rob[0] ==0:
        con[0] -= 1
        rob[0] = level
    if (con.count(0)>=k):
        break
    level += 1

print(level)
