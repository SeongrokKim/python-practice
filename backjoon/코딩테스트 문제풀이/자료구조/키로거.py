t = int(input())
for _ in range(t):
    ll1 = []
    ll2 = []
    s = input()
    l = len(s)
    for i in range(l):
        if s[i] == '<':
            if ll1:
                ll2.append(ll1.pop())
        elif s[i] == '>':
            if ll2:
                ll1.append(ll2.pop())
        elif s[i] == '-':
            if ll1:
                ll1.pop()
        else:
            ll1.append(s[i])
    
    ll1.extend(reversed(ll2))
    answer = ''.join(ll1)
    print(answer)