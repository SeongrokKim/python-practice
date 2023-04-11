from collections import deque

n = int(input())
l = []
d = deque()
answer = []
for i in range(n):
    l.append(int(input()))
cnt = 0
for i in range(n):
    while cnt<l[i]:
        cnt += 1
        d.append(cnt)
        answer.append('+')
    tmp = d.pop()
    if tmp != l[i]:
        print('NO')
        exit(0)
    answer.append('-')

for i in range(len(answer)):
    print(answer[i])