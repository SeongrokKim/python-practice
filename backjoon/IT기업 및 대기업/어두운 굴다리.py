import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int,input().split()))

h = x[0]
if len(x) == 1:
    h = max(x[0], n-x[0])
else:
    now = h + h
    for i in range(1, len(x)):
        if now < x[i]-h:
            h = (x[i] - x[i-1] + 1) // 2
        now = x[i] + h
    if now < n:
        h = n - x[-1]
print(h)

