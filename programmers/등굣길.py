def solution(m, n, puddles):
    answer = 0
    jido = [[0] * (m+1) for i in range(n+1)]
    jido[1][1] = 1
    for puddle in puddles:
        jido[puddle[1]][puddle[0]] = -1
    for i in range(1,n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                pass
            elif jido[i][j] < 0:
                pass
            else:
                if jido[i-1][j] < 0:
                    jido[i][j] = jido[i][j-1]
                elif jido[i][j-1] < 0:
                    jido[i][j] = jido[i-1][j]
                else:
                    jido[i][j] = (jido[i-1][j] + jido[i][j-1]) % 1000000007
    answer = jido[n][m]
    return answer