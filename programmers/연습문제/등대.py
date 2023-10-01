from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    answer = 0
    result = [0 for _ in range(n+1)]
    link = defaultdict(list)
    for s,e in lighthouse:
        link[s].append(e)
        link[e].append(s)
    def dfs(node, parent):
        for child in link[node]:
            if child == parent:
                continue
            dfs(child, node)
            if result[child] == 0 and result[node] == 0:
                result[node] = 1
    dfs(1, 1)
    return result.count(1)