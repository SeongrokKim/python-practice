import sys
from collections import defaultdict
input = sys.stdin.readline

def find(a,b):
    if (a, b) == parent[(a,b)]:
        return (a,b)
    else:
        (c,d) = find(parent[(a,b)][0], parent[(a,b)][1])
        parent[(a,b)] = (c,d)
        return parent[(a,b)]

def union(a, b, c, d):
    (a,b)= find(a,b)
    (c,d)= find(c,d)
    if (a,b)!=(c,d):
        for k, v in parent.items():
            if v == (c, d):
                parent[k]=(a,b)

N, L, R = map(int, input().split())
day = 0
world = []
for _ in range(N):
    inputt = list(map(int,input().split()))
    world.append(inputt)

while True:
    parent = {}
    population = {}
    for i in range(N):
        for j in range(N):
            if (i,j) not in parent:
                parent[(i,j)] = (i,j)
                population[(i,j)] = world[i][j]
                
            if i-1 > -1:
                if (i-1, j) not in parent:
                    parent[(i-1, j)] = (i-1, j)
                    population[(i-1, j)] = world[i-1][j]
                if L <= abs(population[(i,j)] - population[(i-1,j)]) <= R:
                    union(i, j, i-1, j)
            if i+1 < N:
                if (i+1, j) not in parent:
                    parent[(i+1, j)] = (i+1, j)
                    population[(i+1, j)] = world[i+1][j]
                if L <= abs(population[(i,j)] - population[(i+1,j)]) <= R:
                    union(i, j, i+1, j)
            if j-1 > -1:
                if (i, j-1) not in parent:
                    parent[(i, j-1)] = (i, j-1)
                    population[(i, j-1)] = world[i][j-1]
                if L <= abs(population[(i,j)] - population[(i,j-1)]) <= R:
                    union(i, j, i, j-1)
            if j+1 < N:
                if (i, j+1) not in parent:
                    parent[(i, j+1)] = (i, j+1)
                    population[(i, j+1)] = world[i][j+1]
                if L <= abs(population[(i,j)] - population[(i,j+1)]) <= R:
                    union(i, j, i, j+1)
    dict = defaultdict(list)
    for k, v in parent.items():
        dict[v].append(k)
    move = False
    for k, v in dict.items():
        if len(v) > 1:
            tot = 0
            for r, c in v:
                tot += world[r][c]
            for r, c in v:
                world[r][c] = int(tot/len(v))
            move = True
    if move:
        day += 1
    else:
        print(day)
        break