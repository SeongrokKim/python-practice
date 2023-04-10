def solution(s):
    answer = ''
    list1 = s.split()
    list2 = []
    for i in list1:
        list2.append(int(i))
        
    list2.sort()
    answer += str(list2[0]) + ' ' + str(list2[-1])
    return answer