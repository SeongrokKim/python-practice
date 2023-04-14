def solution(N, number):
    answer = 0
    if number == N:
        return 1
    else:
        dic = {}
        dic[1] = {N}
        for i in range(2, 9):
            j = 1
            tmp = {int(str(N)*i)}
            
            def calcul(A, B):
                rst = set()
                for a in A:
                    for b in B:
                        rst.add(a+b)
                        rst.add(a-b)
                        rst.add(a*b)
                        if b != 0:
                            rst.add(a//b)
                return rst
            
            while j < i:
                tmp.update(calcul(dic[j], dic[i-j]))
                j += 1
            if number in tmp:
                return i
            dic[i] = tmp
    
    return -1