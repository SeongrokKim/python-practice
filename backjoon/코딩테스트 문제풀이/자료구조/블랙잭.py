n, m = map(int,input().split())
l=list(map(int,input().split()))
hap = []
for i in range(len(l)-2):
    for j in range(i+1, len(l)-1):
        for k in range(j+1, len(l)):
            hap.append(l[i]+l[j]+l[k])
hap.sort()
idx = 0
while idx<len(hap):
    if hap[idx]>m:
        break
    idx += 1

print(hap[idx-1])