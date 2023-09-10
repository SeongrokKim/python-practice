def solution(arr):
    answer = [0, 0]
    leng = len(arr)
    all_same = True
    while leng > 1:
        for i in range(0, len(arr), leng//2):
            for j in range(0, len(arr), leng//2):
                cap = arr[i][j]
                x = i
                y = j
                same = True
                while x < i+leng//2 and same:
                    while y < j+leng//2 and same:
                        if arr[x][y] == -1:
                            break
                        if arr[x][y] != cap:
                            same = False
                            all_same = False
                        y += 1
                    x += 1
                    y = j
                if same:
                    for x in range(i, i+leng//2):
                        for y in range(j, j+leng//2):
                            arr[x][y] = -1
                    arr[i][j] = cap
        leng //= 2
    if all_same:
        if arr[0][0] == 0:
            return [1, 0]
        else:
            return [0, 1]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                answer[0] += 1
            if arr[i][j] == 1:
                answer[1] += 1
    return answer