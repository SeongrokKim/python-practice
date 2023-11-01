def solution(user_id, banned_id):
    info = []
    
    def same(b, u):
        n = len(b)
        if len(u) != n:
            return False
        for i in range(n):
            if b[i] == '*':
                continue
            else:
                if b[i] != u[i]:
                    return False
        return True
    
    for ban in banned_id:
        user_list = []
        for user in user_id:
            if same(ban, user):
                user_list.append(user)
        info.append(user_list)
    
    cand = set()

    def find_combinations(idx, combination):
        if idx == len(banned_id):
            cand.add(tuple(sorted(combination)))
            return
        for user in info[idx]:
            if user not in combination:
                find_combinations(idx + 1, combination + [user])

    find_combinations(0, [])
    return len(cand)