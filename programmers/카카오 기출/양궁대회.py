from itertools import product
def solution(n, info):
    info.reverse()
    ans = [-1]
    max_dif = 0
    for result in product((True, False), repeat=11):
        s=0
        for i in range(11):
            if result[i]:
                s += info[i]+1
        if s <= n:
            apch = 0
            ryan = 0
            for i in range(11):
                if not result[i] and info[i]:
                    apch += i
                if result[i]:
                    ryan += i
            dif = ryan - apch
            if dif > max_dif:
                max_dif = dif
                ans = []
                for i in range(11):
                    if result[i]:
                        ans.append(info[i]+1)
                    else:
                        ans.append(0)
                ans[0] += n-s
    ans.reverse()
    return ans