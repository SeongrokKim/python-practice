def solution(n, m, x, y, r, c, k):
    answer = ''
    
    diff = abs(x-r) + abs(y-c)
    if abs(diff-k)%2 == 1 or diff > k:
        answer = 'impossible'
    else:
        down = up = left = right = 0
        if r >= x:
            down = r - x
            for _ in range(down):
                answer += 'd'
            if c >= y:
                right = c - y
                k -= down + right
                while k > 0:
                    if r < n :
                        answer += 'd'
                        up += 1
                        r += 1
                        k -= 2
                    elif y > 1:
                        answer += 'l'
                        right += 1
                        y -= 1
                        k -= 2
                    else:
                        break
                if k:
                    while k != 0:
                        answer += 'rl'
                        k -= 2
                for _ in range(right):
                    answer += 'r'
                for _ in range(up):
                    answer += 'u'
            else:
                left = y - c
                k -= down + left
                while k > 0:
                    if r < n :
                        answer += 'd'
                        up += 1
                        r += 1
                        k -= 2
                    elif c > 1:
                        answer += 'l'
                        right += 1
                        c -= 1
                        k -= 2
                    else:
                        break
                for _ in range(left):
                    answer += 'l'
                while k != 0:
                    answer += 'rl'
                    k -= 2
                for _ in range(right):
                    answer += 'r'
                for _ in range(up):
                    answer += 'u'
        else:
            up = x - r
            if c >= y:
                right = c - y
                k -= up + right
                while k > 0:
                    if x < n :
                        answer += 'd'
                        up += 1
                        x += 1
                        k -= 2
                    elif y > 1:
                        answer += 'l'
                        right += 1
                        y -= 1
                        k -= 2
                    else:
                        break
                if k:
                    while k != 0:
                        answer += 'rl'
                        k -= 2
                for _ in range(right):
                    answer += 'r'
                for _ in range(up):
                    answer += 'u'
            else:
                left = y - c
                k -= up + left
                while k > 0:
                    if x < n :
                        answer += 'd'
                        up += 1
                        x += 1
                        k -= 2
                    elif c > 1:
                        answer += 'l'
                        right += 1
                        c -= 1
                        k -= 2
                    else:
                        break
                for _ in range(left):
                    answer += 'l'
                while k != 0:
                    answer += 'rl'
                    k -= 2
                for _ in range(right):
                    answer += 'r'
                for _ in range(up):
                    answer += 'u'
                
    return answer