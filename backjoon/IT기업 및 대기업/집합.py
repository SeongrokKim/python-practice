import sys
input = sys.stdin.readline
s = set()

m = int(input())
for _ in range(m):
    inputt = input().rsplit()
    if inputt[0] == 'all':
        s = set()
        for i in range(1,21):
            s.add(i)
    elif inputt[0] == 'empty':
        s = set()
    elif inputt[0] == 'add':
        s.add(int(inputt[1]))
    elif inputt[0] == 'remove':
        s.discard(int(int(inputt[1])))
    elif inputt[0] == 'check':
        if int(int(inputt[1])) in s:
            print(1)
        else:
            print(0)
    elif inputt[0] == 'toggle':
        if int(int(inputt[1])) in s:
            s.remove(int(int(inputt[1])))
        else:
            s.add(int(int(inputt[1])))
