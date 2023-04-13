import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent=[]
for i in range(n):
    parent.append(i)

def find(x):
    while x!=parent[x]:
        x= parent[x]
    return x

def union(x,y):
    xp = find(x)
    yp = find(y)
    if xp<yp:
        parent[yp]=xp
    elif xp>yp:
        parent[xp]=yp
    else:
        return 0
    return 1


answer = 0
for i in range(m):
    dot1, dot2 = map(int,input().split())
    tmp = union(dot1, dot2)
    if tmp:
        continue
    else:
        answer = i+1
        break

print(answer)