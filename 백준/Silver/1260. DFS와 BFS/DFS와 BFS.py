import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

def bfs(start):
    visited = [False for x in range(100001)]
    
    Q = deque()
    Q.append(start)
    visited[start] = True
    
    while Q :
        node = Q.popleft()
        visited[node] = True
        print(node,end=" ")
        
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                Q.append(n)
                
def dfs(node):
    visited[node] = True
    print(node,end=" ")
    graph[node].sort()
    for n in graph[node]:
        if not visited[n]:        
            dfs(n)
    
    


N, M, V = map(int,input().split())

graph = [[] for x in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False for x in range(10001)]

dfs(V)
print()
bfs(V)