def solution(triangle):
    answer = 0
    idx = 0
    list1 = [0]*len(triangle)
    for i in range(len(triangle)):
        for j in range(i + 1):
            if j == 0:
                list1[0] += triangle[i][0]
            elif j == i:
                list1[j] = list2[j-1] + triangle[i][j]
                
            else:
                list1[j] = max(list2[j-1] + triangle[i][j],list2[j] + triangle[i][j])
        
        list2=list1.copy()
    answer = max(list1)
    return answer