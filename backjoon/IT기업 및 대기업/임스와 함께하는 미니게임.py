import sys
input = sys.stdin.readline
n, type = map(str,input().split())
people = set()
for _ in range(int(n)):
    id = input().rsplit()[0]
    people.add(id)
if type == 'Y':
    print(len(people))
elif type == 'F':
    print(len(people)//2)
else:
    print(len(people)//3)