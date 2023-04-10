from collections import deque

def bfs(now, target, words, deque, ans):
    if now == target:
        return ans
    else:
        ans = deque[0][1] + 1
        deque.popleft()
        for word in words:
            dif = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    dif += 1
            if dif == 1:
                deque.append([word, ans])
                words.remove(word)
        now = deque[0][0]
        ans = deque[0][1]
        return bfs(now, target, words, deque, ans)
        
    
def solution(begin, target, words):
    answer = 0
    deq = deque()
    deq.append([begin, answer])
    if target not in words:
        return 0
    answer = bfs(begin, target, words, deq, answer)
    return answer