import sys
input = sys.stdin.readline

h, w = map(int,input().split())
blocks = list(map(int,input().split()))
start = blocks[0]
rain = []
answer = 0
for i in range(1, w):
    if blocks[i] <= start:
        if rain:
            if min(rain) < blocks[i]:
                for j in range(len(rain)):
                    if rain[j] < blocks[i]:
                        dif = blocks[i] - rain[j]
                        answer += dif
                        rain[j] += dif
        rain.append(blocks[i])
        if blocks[i] == start:
            rain = []
    else:
        if rain:
            for j in range(len(rain)):
                answer += start-rain[j]
        start = blocks[i]
        rain = []
print(answer)