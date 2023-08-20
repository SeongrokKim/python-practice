import sys

input = sys.stdin.readline()
h, w, n, m = map(int, input.split())
print(((h+n)//(1+n)) * ((w+m)//(1+m)))