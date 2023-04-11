answer = 0

def checking(arr,n):
    global answer
    
    n = int(n)
    if len(arr) == n:
        answer += 1
        return
    
    for i in range(n):
        if len(arr) == 0:
            arr.append(i)
            checking(arr,n)
            arr.pop()
        else:
            for i in range(n):
                if i not in arr:
                    can = 1
                    for j in range(len(arr)):
                        if abs(len(arr)) - j == abs(i - arr[j]):
                            can = 0
                            break
                    if can:
                        arr.append(i)
                        checking(arr,n)
                        arr.pop()
            return
                
    
    return
            

def solution(n):
    global answer
    q = []
    checking(q,n)
    
    return answer