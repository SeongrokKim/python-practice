def solution(numbers):
    answer = []
    
    def makeBiNum(num):
        result = []
        while num > 0:
            result.append(str(num%2))
            num //= 2
        result.reverse()
        return ''.join(result)
    
    def check(num, idx, h):
        if h == 2:
            if num[idx] == '1':
                return True
            else:
                if num[idx-1] == '0' and num[idx+1] == '0':
                    return True
                else:
                    return False
        else:
            if num[idx] == '1':
                return check(num, idx - (2**(h-2)), h-1) and check(num, idx + (2**(h-2)), h-1)
            else:
                if num[idx - (2**(h-2))] == '1' or num[idx + (2**(h-2))] == '1':
                    return False
                else:
                    return check(num, idx - (2**(h-2)), h-1) and check(num, idx + (2**(h-2)), h-1)
    
    def checkPossibleToTree(num):
        numLen = len(num)
        h = 1
        while numLen > 2**h -1:
            h += 1
        if h == 1:
            return True
        numOfNode = 2**h - 1
        numList = list(num)
        numList.reverse()
        for _ in range(numOfNode-numLen):
            numList.append("0")
        numList.reverse()
        num = ''.join(numList)
        if check(num, numOfNode//2, h):
            return True
        else:
            return False
    
    for number in numbers:
        biNum = makeBiNum(number)
        if checkPossibleToTree(biNum):
            answer.append(1)
        else:
            answer.append(0)
    return answer
