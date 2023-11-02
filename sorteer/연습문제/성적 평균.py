import sys
n, k = map(int,input().split())
score = list(map(int,input().split()))
for i in range(n-1):
  score[i+1] += score[i]
for i in range(k):
  s, e = map(int,input().split())
  if s == 1:
    print(round((score[e-1])/(e-s+1),2))
  else:
    print(round((score[e-1]-score[s-2])/(e-s+1),2))