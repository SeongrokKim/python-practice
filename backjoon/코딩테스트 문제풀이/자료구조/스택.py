import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        l.append(command[1])
    elif command[0] == 'pop':
        if len(l):
            print(l.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(l))
    elif command[0] == 'empty':
        if len(l):
            print(0)
        else:
            print(1)
    else:
        if len(l):
            print(l[-1])
        else:
            print(-1)