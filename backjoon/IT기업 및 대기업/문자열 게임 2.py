import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input().rsplit()[0]
    k = int(input())
    ans3 = 10001
    ans4 = 0
    if k == 1:
        print(1, 1)
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        l = [[] for _ in range(26)]
        for i in range(len(w)):
            l[alphabet.index(w[i])].append(i)
        for i in range(26):
            if len(l[i]) >= k:
                for j in range(len(l[i])-k+1):
                    ans3 = min(ans3, l[i][j+k-1]-l[i][j]+1)
                    ans4 = max(ans4, l[i][j+k-1]-l[i][j]+1)


        if ans3 == 10001 or ans4 == 0:
            print(-1)
        else:
            print(ans3, ans4)

