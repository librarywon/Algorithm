import sys
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    
    for d in graph[node]:
        if not visited[d]:
            dfs(d)

V = int(input())
E = int(input())

visited = [False for x in range(V+1)]
graph = [ [] for x in range(V+1)]


for x in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

cnt = 0

for i in visited:
    if i is True:
        cnt += 1
print(cnt-1)
