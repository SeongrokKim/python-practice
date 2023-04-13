from itertools import product
def solution(word):
    dic = []
    alpha = 'AEIOU'
    for i in range(1, 6):
        dic += list(product(alpha,repeat=i))
        
    newdic = []
    for d in dic:
        newdic.append(''.join(d))
    newdic.sort()
    answer = newdic.index(word)+1
    return answer