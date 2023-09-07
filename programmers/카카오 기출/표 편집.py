class Node:
    def __init__(self, left = None, right = None):
        self.removed = False
        self.left = left
        self.right = right

def solution(n, k, cmd):
    answer = ""
    table = [Node(i-1,i+1) for i in range(n)]
    table[0].left = None
    table[n-1].right = None
    removed_stack = []
    now = k
    for c in cmd:
        act = c[0]
        if act == 'U':
            cnt = int(c.split()[1])
            for _ in range(cnt):
                now = table[now].left
        elif act == 'D':
            cnt = int(c.split()[1])
            for _ in range(cnt):
                now = table[now].right
        elif act == 'C':
            removed_stack.append(now)
            table[now].removed = True
            left = table[now].left
            right = table[now].right
            if left or left == 0:
                table[left].right = right
            if right:
                table[right].left = left
                now = right
            else:
                now = left
        else:
            save = removed_stack.pop()
            table[save].removed = False
            left = table[save].left
            right = table[save].right
            if left:
                table[left].right = save
            if right:
                table[right].left = save
    
    for i in range(n):
        if table[i].removed:
            answer += "X"
        else:
            answer += "O"
    return answer