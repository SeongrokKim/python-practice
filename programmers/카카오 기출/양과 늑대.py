from collections import defaultdict

def dfs(cur,visited,sheep,wolf,k,dic,info,stack):
    switch=False
    if info[cur]==0 and cur not in stack:
        sheep+=1
        visited=[0 for _ in range(len(info))]
        visited[cur] = 1
        k.append(sheep)
        stack.append(cur)
        switch=True
    if info[cur]==1 and cur not in stack:
        wolf+=1
        stack.append(cur)
        switch=True
    if sheep==wolf:
        visited[cur] = 0
        if switch==True:
            stack.pop()
        return
    for node in dic[cur]:
        if visited[node] == 0:
            visited[node]=1
            dfs(node,visited,sheep,wolf,k,dic,info,stack)
    visited[cur] = 0
    if switch==True:
        stack.pop()

def solution(info, edges):
    answer = []
    dic=defaultdict(list)
    for edge in edges:
        dic[edge[0]].append(edge[1])
        dic[edge[1]].append(edge[0])
    visited = [0 for _ in range(len(info))]
    stack=[]
    dfs(0,visited,0,0,answer,dic,info,stack)
    answer.sort()
    return answer[-1]