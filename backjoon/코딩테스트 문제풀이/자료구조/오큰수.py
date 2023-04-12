import sys
input = sys.stdin.readline

n = int(input())
l=list(map(int, input().split()))
oks=[-1] * n
stack = []
for i in range(n):
    while len(stack) > 0 and stack[len(stack)-1][0] < l[i]:
        oks[stack[-1][1]] = l[i]
        stack.pop()
    stack.append([l[i],i])

for i in range(n):
    print(oks[i], end=' ')