def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
        
    alp = min(alp,max_alp)
    cop = min(cop,max_cop)
    
    dp = [[int(1e9) for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            for problem in problems:
                if problem[0] <= i and problem[1] <= j:
                    dp[min(i + problem[2], max_alp)][min(j + problem[3], max_cop)] = min(dp[min(i + problem[2], max_alp)][min(j + problem[3], max_cop)], dp[i][j] + problem[4])
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
    return dp[-1][-1]