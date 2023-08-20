import sys
input = sys.stdin.readline

def lineUp(arr):
    num = 0
    line = [int(arr[1])]
    for i in range(2, 21):
        line.append(int(arr[i]))
        for j in range(len(line)-1):
            if line[j]>int(arr[i]):
                tmp = int(arr[i])
                for k in range(len(line)-1,j,-1):
                    line[k] = line[k-1]
                    num += 1
                line[j] = tmp
                break

    return num


p = int(input())
for _ in range(p):
    inputt = input().rsplit()
    cnt = lineUp(inputt)
    print(inputt[0], cnt)