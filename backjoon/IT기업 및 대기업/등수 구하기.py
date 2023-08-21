import sys
input = sys.stdin.readline

n, score, p  = map(int,input().split())
l = list(map(int,input().split()))
if n >= p:
    if l[n-1] >= score:
        print(-1)
        exit()
l.append(score)
l.sort(reverse=True)
print(l.index(score)+1)