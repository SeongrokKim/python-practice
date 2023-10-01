from collections import defaultdict
import sys
sys.setrecursionlimit(int(1e6))
cache = defaultdict(dict)
weights = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
]

def solve(i, left, right, numbers):
    if i == len(numbers):
        return 0
    
    if (left, right) in cache[i]:
        return cache[i][(left, right)]
    
    w = int(1e9)
    num = numbers[i]
    if num != right:
        w = min(w, solve(i+1, num, right, numbers) + weights[left][num])
    if num != left:
        w = min(w, solve(i+1, left, num, numbers) + weights[right][num])
        
    cache[i][(left, right)] = w
    return w

def solution(numbers):
    numbers = [int(x) for x in numbers]
    answer = solve(0, 4, 6, numbers)
    return answer