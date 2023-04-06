r,c,k = map(int, input().split())
r -= 1
c -= 1

a=[]
for i in range(3):
    a.append(list(map(int,input().split())))

t = 0

def func(a):
    rowlen = len(a)
    collen = len(a[0])
    maxlen = 0
    newmat = []
    if rowlen>=collen:
        for i in range(rowlen):
            while 0 in a[i]:
                a[i].remove(0)
            sortrow = sorted(a[i])
            newrow = []
            cntrow = []
            for j in range(len(a[i])):
                cntrow.append(a[i].count(sortrow[j]))
            dic = {}
            for j in range(len(a[i])):
                dic[sortrow[j]] = cntrow[j]
            if 0 in a[i]:
                del dic[0]
            sortdic = sorted(dic, key=lambda x:dic[x])
            for j in range(len(sortdic)):
                newrow.append(sortdic[j])
                newrow.append(dic[sortdic[j]])
                
            newmat.append(newrow)
            if maxlen<len(newrow):
                maxlen = len(newrow)
        for i in range(rowlen):
            tmp = len(newmat[i])
            while tmp<maxlen:
                newmat[i].append(0)
                tmp +=1
        a.clear()
        for i in range(len(newmat)):
            a.append(newmat[i])
                
    else:
        newa=[[0 for _ in range(rowlen)] for _ in range(collen)]
        for i in range(collen):
            for j in range(rowlen):
                newa[i][j] = a[j][i]
        a.clear()
        for i in range(len(newa)):
            a.append(newa[i])
        rowlen=len(a)
        collen=len(a[0])
        for i in range(rowlen):
            while 0 in a[i]:
                a[i].remove(0)
            sortrow = sorted(a[i])
            newrow = []
            cntrow = []
            for j in range(len(a[i])):
                cntrow.append(a[i].count(sortrow[j]))
            dic = {}
            for j in range(len(a[i])):
                dic[sortrow[j]] = cntrow[j]
            sortdic = sorted(dic, key=lambda x:dic[x])
            for j in range(len(sortdic)):
                newrow.append(sortdic[j])
                newrow.append(dic[sortdic[j]])
            newmat.append(newrow)
            if maxlen<len(newrow):
                maxlen = len(newrow)
        for i in range(rowlen):
            tmp = len(newmat[i])
            while tmp<maxlen:
                newmat[i].append(0)
                tmp +=1
        a=[[0 for _ in range(len(newmat))] for _ in range(len(newmat[0]))]
        for i in range(len(newmat[0])):
            for j in range(len(newmat)):
                a[i][j] = newmat[j][i]
    
    return a

while t<101:
    if r<len(a) and c<len(a[0]):
        if a[r][c]==k:
            break
    a = func(a)
    t += 1

if t == 101:
    print(-1)
else:
    print(t)