import sys
input = sys.stdin.readline

switchNum = int(input())
state = list(map(int, input().split()))
stuNum = int(input())
student = []
for _ in range(stuNum):
    student.append(list(map(int,input().split())))

for stu in student:
    sex, num = stu
    if sex == 1:
        for i in range(switchNum):
            if (i+1) % num == 0:
                state[i] = (state[i]-1) * (-1)
    else:
        center = num - 1
        dis = 1
        while center - dis >= 0 and center + dis < switchNum:
            if state[center - dis] == state[center + dis]:
                dis += 1
            else:
                break
        for i in range(center-dis + 1, center + dis):
            state[i] = (state[i]-1) * (-1)
line = (switchNum-1) // 20
last = switchNum - line * 20
cnt = 0
while line > 0:
    for i in range(19):
        print(state[cnt*20 + i], end=' ')
    print(state[cnt*20 + 19])
    cnt += 1
    line -= 1

for i in range(last-1):
    print(state[cnt*20 + i], end=' ')
print(state[cnt*20 + last-1])