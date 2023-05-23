import sys
from collections import deque
def bfs(start):
    cnt=0
    Q = deque()
    Q.append(start)
    visited[start] = True
    while Q :
        node=Q.popleft()
        visited[node]=True
        for d in graph[node] :
            if not visited[d]:
                visited[d] = True
                cnt+=1
                Q.append(d)
    return cnt
input = sys.stdin.readline

V = int(input())
E = int(input())
graph = [ [] for x in range(V+1)]

for i in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for x in range(V+1)]
cnt=0
print(bfs(1))