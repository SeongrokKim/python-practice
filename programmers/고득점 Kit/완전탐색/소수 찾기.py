from itertools import permutations

def checkPrime(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
        return True
    

def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))
    print(per)
    new = [int("".join(p)) for p in per]
    
    for n in new:
        if checkPrime(n):
            answer.append(n)
    return len(set(answer))