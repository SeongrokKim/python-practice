def solution(price, money, count):
    need = 0
    for i in range(1, count+1):
        need += price*i
    if need>money:
        answer = need-money
    else:
        answer = 0
    return answer