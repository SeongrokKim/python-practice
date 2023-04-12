import sys
input = sys.stdin.readline

k = int(input())
l = []
for _ in range(k):
    num = int(input())
    if num:
        l.append(num)
    else:
        if len(l):
            l.pop()
print(sum(l))