import sys
input = sys.stdin.readline

n,m= map(int, input().split())

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

for i in range(m):
    dot1, dot2 = map(int,input().split())
    union(dot1-1, dot2-1)

for i in range(n):
    parent[i] = find(i)

s=set(parent)
print(len(s))