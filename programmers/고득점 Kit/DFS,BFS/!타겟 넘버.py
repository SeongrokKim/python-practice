def solution(numbers, target):
    def dfs(numbers, target, idx):
        answer = 0
        if idx == len(numbers):
            if sum(numbers) == target:
                return 1
            return 0
        else:
            answer += dfs(numbers, target, idx+1)
            numbers[idx] *= -1
            answer += dfs(numbers, target, idx+1)
            return answer
            
    answer = dfs(numbers, target, 0)
    return answer