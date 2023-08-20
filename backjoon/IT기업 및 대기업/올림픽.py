import sys
input = sys.stdin.readline

n, k = map(int, input().split())
results = [[] for _ in range(n)]
rank = 0

for i in range(n):
    result = list(map(int,input().split()))
    results[i] = result
results.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(n):
    if results[i][0]==k:
        rank = i
        break

while rank>0:
    if results[rank-1][1:] == results[rank][1:]:
        rank -= 1
    else:
        break

print(rank + 1)