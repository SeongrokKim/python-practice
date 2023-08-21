import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    result = list(map(int,input().split()))
    dict = defaultdict(list)
    score = []
    for i in range(n):
        dict[result[i]].append(i)
        score.append(i)
    fail = []
    for team, rank in dict.items():
        if len(rank) < 6:
            fail.append((team, rank))
            for r in rank:
                score[r] = -1
    for team, rank in fail:
        dict.pop(team)
    s = 1
    for i in range(len(score)):
        if score[i] == -1:
            continue
        else:
            score[i] = s
            s += 1
    
    tot = 1e9
    winner = []
    for team, rank in dict.items():
        if len(rank) == 6:
            teamScore = 0
            for i in range(4):
                teamScore += score[rank[i]]
            if teamScore < tot:
                tot = teamScore
                winner = rank
                answer = team
            elif teamScore == tot:
                if rank[4] < winner[4]:
                    winner = rank
                    answer = team
    print(answer)

