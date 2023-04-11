def solution(land):
    answer = 0
    
    arr = [0, 0, 0, 0]
    for i in range(len(land)):
        land[i][0] = max(land[i][0] + arr[1], land[i][0] + arr[2], land[i][0] + arr[3])
        land[i][1] = max(land[i][1] + arr[0], land[i][1] + arr[2], land[i][1] + arr[3])
        land[i][2] = max(land[i][2] + arr[0], land[i][2] + arr[1], land[i][2] + arr[3])
        land[i][3] = max(land[i][3] + arr[0], land[i][3] + arr[1], land[i][3] + arr[2])
        arr = land[i]
    answer = max(arr)
    return answer