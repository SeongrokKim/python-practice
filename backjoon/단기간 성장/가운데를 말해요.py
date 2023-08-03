import sys
import heapq
input = sys.stdin.readline
n = int(input())
leftQueue = []
rightQueue = []
for i in range(n):
    num = int(input())
    if len(leftQueue) == len(rightQueue):
        heapq.heappush(leftQueue, -num)
    else:
        heapq.heappush(rightQueue, num)
    if rightQueue:
        if -leftQueue[0] > rightQueue[0]:
            maxLeft = -heapq.heappop(leftQueue)
            minRight = heapq.heappop(rightQueue)
            heapq.heappush(leftQueue, -minRight)
            heapq.heappush(rightQueue, maxLeft)
    
    print(-leftQueue[0])