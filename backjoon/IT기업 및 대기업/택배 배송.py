import sys
import heapq
input = sys.stdin.readline

n, m = map(int,input().split())
leastFeed = [int(1e9) for _ in range(n+1)]
leastFeed[1] = 0
infos = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    infos[a].append((b,c))
    infos[b].append((a,c))

q = []
heapq.heappush(q, (0, 1))
while q:
    lf, now = heapq.heappop(q)
    if leastFeed[now] >= lf:
        for i in infos[now]:
            feed = lf + i[1]
            if feed < leastFeed[i[0]]:
                leastFeed[i[0]] = feed
                heapq.heappush(q, (feed, i[0]))

print(leastFeed[n])
