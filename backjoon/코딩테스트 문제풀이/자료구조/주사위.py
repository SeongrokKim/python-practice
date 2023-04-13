import sys
input = sys.stdin.readline

s1, s2, s3 = map(int,input().split())

dic = {}
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            if i+j+k not in dic:
                dic[i+j+k] = 1
            else:
                dic[i+j+k] += 1
sortDic = sorted(dic.items(), key=lambda x: x[1], reverse= True)
print(sortDic[0][0])