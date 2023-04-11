n = int(input())
a = {}
b = list(map(int, input().split()))
for i in range(n):
    a[b[i]] = 1
m = int(input())
l = list(map(int, input().split()))
for i in range(m):
    if l[i] in a:
        print(1)
    else:
        print(0)