import sys
input = sys.stdin.readline

n = int(input())
topList = [100000001]
topList += list(map(int,input().split()))
receiver = [(0,100000001)]
for i in range(2, n+1):
    if topList[i] < topList[i-1]:
        receiver.append((i-1, topList[i-1]))
    elif topList[i] == topList[i-1]:
        receiver.append((i-1, topList[i]))
    else:
        if topList[i] <= receiver[i-2][1]:
            receiver.append((receiver[i-2]))
        else:
            for j in range(receiver[i-2][0]-1,-1,-1):
                if topList[j] >= topList[i]:
                    receiver.append((j, topList[j]))
                    break
for i in range(n):
    print(receiver[i][0], end=' ')