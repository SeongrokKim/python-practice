import sys
input = sys.stdin.readline

n = int(input())
m = []
x = y = 0
for _ in range(n):
    m.append(input().rsplit()[0])
for i in range(n):
    if '*' in m[i]:
        x = i+2
        y = m[i].find('*')+1
        print(x, y)
        break
leftArm = rightArm = waist = leftLeg = rightLeg = 0
for i in range(y-2, -1, -1):
    if m[x-1][i] == '*':
        leftArm += 1
    else:
        break
for i in range(y, n):
    if m[x-1][i] == '*':
        rightArm += 1
    else:
        break
endOfWaist = 0
for i in range(x,n):
    if m[i][y-1] == '*':
        waist += 1
    else:
        endOfWaist = i
        break
for i in range(endOfWaist, n):
    if m[i][y-2] == '*':
        leftLeg += 1
    if m[i][y] == '*':
        rightLeg += 1
    if m[i][y-2] == '_' and m[i][y] == '_':
        break
print(leftArm, rightArm, waist, leftLeg, rightLeg)