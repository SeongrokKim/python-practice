def solution(phone_book):
    answer = True
    hash_table = {}
    for p in phone_book:
        for i in range(1,len(p)):
            hash_table[p[:i]] = 1
    for p in phone_book:
        if p in hash_table:
            return False
    
    return answer