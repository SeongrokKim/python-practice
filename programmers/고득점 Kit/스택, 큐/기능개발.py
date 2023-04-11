def solution(progresses, speeds):
    answer = []
    num = len(progresses)
    while num > 0:
        while progresses[0] < 100:
            for i in range(num):
                progresses[i] += speeds[i]
        cnt = 0
        while len(progresses)>0 and progresses[0] >= 100:
            cnt += 1
            progresses.remove(progresses[0])
            speeds.remove(speeds[0])
        answer.append(cnt)
        num -= cnt
    return answer