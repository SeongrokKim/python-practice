import sys
input = sys.stdin.readline

s= input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for a in alphabet:
    if a in s:
        print(s.index(a), end=' ')
    else:
        print('-1', end=' ')