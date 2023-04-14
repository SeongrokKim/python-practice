n = int(input())
info = []
info.append([0,0,0,0])
for i in range(n):
    s, h, w = map(int,input().split())
    info.append([i, s, h, w])
info.sort(key=lambda x:(x[1]))
high = [0]*(n+1)
for i in range(1, n+1):
    for j in range(0,i):
        if info[i][3] > info[j][3]:
            high[i] = max(high[i], high[j] + info[i][2])
maxval = max(high)
index = n
result = []
while index > 0:
    if maxval == high[index]:
        result.append(info[index][0])
        maxval -= info[index][2]
    index -= 1
print(len(result))
for i in range(len(result)):
    print(result[len(result)-i-1]+1)