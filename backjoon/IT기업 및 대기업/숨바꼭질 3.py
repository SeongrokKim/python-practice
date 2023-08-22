from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
visited = [-1] * 100001
visited[n] = 0
q = deque()
q.appendleft(n)
while q:
    now = q.pop()
    if now == k:
        print(visited[now])
        break
    if 0 <= now-1 < 100001 and visited[now-1] == -1:
        q.appendleft(now-1)
        visited[now-1] = visited[now] + 1
    if 0 < now*2 < 100001 and visited[now*2] == -1:
        q.append(now*2)
        visited[now*2] = visited[now]
    if 0 <= now+1 < 100001 and visited[now+1] == -1:
        q.appendleft(now+1)
        visited[now+1] = visited[now] +1
    
    