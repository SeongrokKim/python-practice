def solution(e, starts):
    answer = []
    times = [0 for _ in range(e+1)]
    for i in range(2, e + 1):
        for j in range(1,min(e//i+1,i)):
            times[i*j] += 2
    for i in range(1,int(e**(1/2))+1):
        times[i**2]+=1
    result = [0 for _ in range(e+1)]
    max_count = 0
    for idx in range(e, 0, -1):
        if max_count <= times[idx]:
            max_count = times[idx]
            result[idx] = idx
        else:
            result[idx] = result[idx + 1]
    for s in starts:
        answer.append(result[s])
    return answer