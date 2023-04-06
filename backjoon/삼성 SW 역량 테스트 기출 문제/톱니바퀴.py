from collections import deque

a=deque()
b=deque()
c=deque()
d=deque()
state=[]
for i in range(4):
    state.append(input())
    for j in range(8):
        if i == 0:
            a.append(int(state[i][j]))
        if i == 1:
            b.append(int(state[i][j]))
        if i == 2:
            c.append(int(state[i][j]))
        if i == 3:
            d.append(int(state[i][j]))

def topni(n, w):
    if w == 1:
        if n == 1:
            if a[2] != b[6]:
                if b[2] != c[6]:
                    if c[2] != d[6]:
                        d.rotate(-1)
                    c.rotate(1)
                b.rotate(-1)
            a.rotate(1)
        elif n == 2:
            if a[2] != b[6]:
                a.rotate(-1)
            if b[2] != c[6]:
                if c[2] != d[6]:
                    d.rotate(1)
                c.rotate(-1)
            b.rotate(1)
        elif n == 3:
            if c[2] != d[6]:
                d.rotate(-1)
            if b[2] != c[6]:
                if b[6] != a[2]:
                    a.rotate(1)
                b.rotate(-1)
            c.rotate(1)
        else:
            if c[2] != d[6]:
                if b[2] != c[6]:
                    if b[6] != a[2]:
                        a.rotate(-1)
                    b.rotate(1)
                c.rotate(-1)
            d.rotate(1)

    else:
        if n == 1:
            if a[2] != b[6]:
                if b[2] != c[6]:
                    if c[2] != d[6]:
                        d.rotate(1)
                    c.rotate(-1)
                b.rotate(1)
            a.rotate(-1)
        elif n == 2:
            if a[2] != b[6]:
                a.rotate(1)
            if b[2] != c[6]:
                if c[2] != d[6]:
                    d.rotate(-1)
                c.rotate(1)
            b.rotate(-1)
        elif n == 3:
            if c[2] != d[6]:
                d.rotate(1)
            if b[2] != c[6]:
                if b[6] != a[2]:
                    a.rotate(-1)
                b.rotate(1)
            c.rotate(-1)
        else:
            if c[2] != d[6]:
                if b[2] != c[6]:
                    if b[6] != a[2]:
                        a.rotate(1)
                    b.rotate(-1)
                c.rotate(1)
            d.rotate(-1)

k = int(input())

for i in range(k):
    num, way = map(int,input().split())
    topni(num,way)

answer = a[0]+b[0]*2+c[0]*4+d[0]*8
print(answer)