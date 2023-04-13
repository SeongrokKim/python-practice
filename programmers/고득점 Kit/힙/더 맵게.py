from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0]<K and len(scoville)>1:
        a = heappop(scoville)
        b = heappop(scoville)
        if a == 0 and b == 0:
            return -1
        heappush(scoville, a+b*2)
        answer += 1
    if len(scoville)==1 and scoville[0]<K or len(scoville)==0:
        return -1
    return answer