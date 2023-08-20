import sys

while True:
    input = sys.stdin.readline()
    a, b, c = map(int, input.split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        l = [a, b, c]
        l.sort()
        if l[2] >= l[0] + l[1]:
            print('Invalid')
        elif a == b and b == c:
            print('Equilateral')
        elif a != b and b != c and c != a:
            print('Scalene')
        elif (a == b and c != a) or (b == c and a != b) or (c == a and b != c):
            print('Isosceles')
        else:
            print('Invalid')