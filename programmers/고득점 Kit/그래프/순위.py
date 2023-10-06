def solution(n, results):
    answer = 0
    result = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for w, l in results:
        result[w][l] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if result[j][k]==0 and result[j][i] == 1 and result[i][k] == 1:
                    result[j][k] = 1
    answers = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if result[i][j] == 1:
                answers[i] += 1
                answers[j] += 1
    for i in range(n+1):
        if answers[i] == n-1:
            answer += 1
    return answer