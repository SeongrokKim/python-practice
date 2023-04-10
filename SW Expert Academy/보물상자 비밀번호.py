T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, k = map(int, input().split())
    l = input()
    box = [[0 for _ in range(n//4)] for _ in range(4)]
    idx = 0
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    alphaDic = {}
    for i in range(6):
        alphaDic[alpha[i]] = i + 10
    for i in range(4):
        for j in range(n//4):
            box[i][j] = l[idx]
            idx += 1
            
    numSet = []
    for i in range(4):
        b = ''
        for j in range(n//4):
            b += box[i][j]
        numSet.append(b)
    for i in range(n//4):
        l = l[-1] + l[0:len(l)-1]
        idx = 0
        for w in range(4):
            for j in range(n//4):
                box[w][j] = l[idx]
                idx += 1
        for j in range(4):
            b = ''
            for w in range(n//4):
                b += box[j][w]
            if b not in numSet:
                numSet.append(b)
    numDic = {}            
    for i in range(len(numSet)):
        decNum = 0
        jarisoo = n//4 - 1
        for j in range(n//4):
            if numSet[i][j] in alpha:
                tmp = alphaDic[numSet[i][j]]
            else:
                tmp = int(numSet[i][j])
            decNum += tmp * 16 ** jarisoo
            jarisoo -= 1
        numDic[numSet[i]] = decNum
    sortedNumList = sorted(numDic.values(), reverse = True)
    print("#{} {}".format(test_case, sortedNumList[k-1]))
    # ///////////////////////////////////////////////////////////////////////////////////
