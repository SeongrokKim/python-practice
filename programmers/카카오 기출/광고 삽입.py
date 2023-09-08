def timeToSec(time):
    h, m, s = time.split(":")
    sec = 0
    if h != "00":
        if h[0] == "0":
            sec += 3600 * int(h[1])
        else:
            sec += 3600 * int(h)
    if m != "00":
        if m[0] == "0":
            sec += 60 * int(m[1])
        else:
            sec += 60 * int(m)
    sec += int(s)
    return sec

def secToTime(sec):
    time = ''
    h = sec // 3600
    m = (sec - 3600*h) // 60
    s = sec % 60
    if h >= 10:
        time = str(h) + ":"
    else:
        time = "0" + str(h) + ":"
    if m >= 10:
        time += str(m) + ":"
    else:
        time += "0" + str(m) + ":"
    if s >= 10:
        time += str(s)
    else:
        time += "0" + str(s)
    return time

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    answer = 0
    play = timeToSec(play_time)
    adv = timeToSec(adv_time)
    max_time = 0
    viewer_num = [0 for _ in range(play+1)]
    for log in logs:
        start, finish = log.split("-")
        viewer_num[timeToSec(start)] += 1
        viewer_num[timeToSec(finish)] -= 1
    for i in range(1, play+1):
        viewer_num[i] += viewer_num[i-1]
    prefix_sum = [0]
    total = 0
    for i in range(len(viewer_num)):
        total += viewer_num[i]
        prefix_sum.append(total)
    for start in range(len(viewer_num)):
        if start+1+adv >= len(prefix_sum):
            break
        total_time = prefix_sum[start+adv] - prefix_sum[start]
        if total_time > max_time:
            max_time = total_time
            answer = start
    return secToTime(answer)