def solution(jobs):
    answer = 0
    sortJob = sorted(jobs, key=lambda x:(x[1], x[0]))
    start = sorted(jobs)
    numJob = len(jobs)
    finTime = start[0][0] + start[0][1]
    cnt = 1
    answer = start[0][1]
    sortJob.remove([start[0][0], start[0][1]])
    while cnt<numJob:
        find = False
        for j in sortJob:
            if j[0] <= finTime:
                finTime += j[1]
                answer += finTime - j[0]
                sortJob.remove(j)
                cnt += 1
                find = True
                break
        if find:
            continue
        else:
            nextjob = sorted(sortJob)[0]
            finTime = nextjob[0] + nextjob[1]
            answer += nextjob[1]
            sortJob.remove(nextjob)
            cnt += 1
    return answer//numJob