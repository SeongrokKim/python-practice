from itertools import permutations
def solution(k, dungeons):
    hp = k
    answer = 0
    per = []
    for i in range(1, len(dungeons)+1):
        per += list(permutations(dungeons,i))
    for p in per:
        k = hp
        cnt = 0
        leng = len(p)
        while cnt<leng:
            if p[cnt][0]<=k:
                k -= p[cnt][1]
            else:
                break
            cnt += 1
        answer = max(answer, cnt)
    return answer