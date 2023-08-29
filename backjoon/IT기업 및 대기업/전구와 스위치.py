import sys
input = sys.stdin.readline

n = int(input())
now = []
want = []
for e in list(input().rsplit()[0]):
    now.append(int(e))
for e in list(input().rsplit()[0]):
    want.append(int(e))

def check(now, want):
    this = now[:]
    a = 0
    for i in range(1, n):
        if this[i-1] != want[i-1]:
            for j in range(i-1,i+2):
                if j < n:
                    this[j] = 1 - this[j]
            a += 1
    if this == want:
        return a
    return int(1e9)

answer1 = check(now, want)
now[0] = 1 - now[0]
now[1] = 1 - now[1]
answer2 = check(now, want) + 1
answer = min(answer1, answer2)
if answer != int(1e9):
    print(answer)
else:
    print(-1)

