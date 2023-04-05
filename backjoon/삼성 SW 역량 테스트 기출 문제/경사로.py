n,l = map(int,input().split())
jido = []
for i in range(n):
    jido.append(list(map(int,input().split())))
    

answer = 0
for i in range(n):
    has = [ 0 for _ in range(n)]
    j = 0
    while(j<n-1):
        if jido[i][j]-jido[i][j+1] > 1 or jido[i][j] - jido[i][j+1] < -1:
            break
        elif jido[i][j]-jido[i][j+1] == 1:
            if l == 1:
                j += 1
                has[j] = 1
            else:
                leng = 1
                k=1
                while(leng != l and j+k+1<n):
                    if jido[i][j+k] == jido[i][j+k+1]:
                        leng+=1
                        k+=1
                    else:
                        break
                if leng == l:
                    j += k
                    has[j] = 1
                else:
                    break
        elif jido[i][j]-jido[i][j+1] == -1:
            if has[j] == 1:
                break
            else:
                if l == 1:
                    has[j]=1
                    j += 1
                else:
                    leng = 1
                    k = 1
                    while(leng != l and j-k>-1):
                        if jido[i][j] == jido[i][j-k]:
                            if has[j-k] == 1:
                                break
                            leng+=1
                            k+=1
                        else:
                            break
                    if leng == l:
                        has[j]=1
                        j += 1
                    else:
                        break
        else:
            j += 1

    if j == n-1:
        answer += 1

for i in range(n):
    has = [ 0 for _ in range(n)]
    j = 0
    while(j<n-1):
        if jido[j][i]-jido[j+1][i] > 1 or jido[j][i] - jido[j+1][i] < -1:
            break
        elif jido[j][i]-jido[j+1][i] == 1:
            if l == 1:
                j += 1
                has[j] = 1
            else:
                leng = 1
                k=1
                while(leng != l and j+k+1<n):
                    if jido[j+k][i] == jido[j+k+1][i]:
                        leng+=1
                        k+=1
                    else:
                        break
                if leng == l:
                    j += k
                    has[j] = 1
                else:
                    break
        elif jido[j][i]-jido[j+1][i] == -1:
            if has[j] == 1:
                break
            else:
                if l == 1:
                    has[j]=1
                    j += 1
                else:
                    leng = 1
                    k = 1
                    while(leng != l and j-k>-1):
                        if jido[j][i] == jido[j-k][i]:
                            if has[j-k] == 1:
                                break
                            leng+=1
                            k+=1
                        else:
                            break
                    if leng == l:
                        has[j]=1
                        j += 1
                    else:
                        break
        else:
            j += 1

    if j == n-1:
        answer += 1

print(answer)