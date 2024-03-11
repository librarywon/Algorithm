import sys
input = sys.stdin.readline
from collections import deque


max = 1

def bfs(starti,startj,height):
    
    if visited[starti][startj] or graph[starti][startj]< height :
        return 0
    
    Q = deque() # 큐
    Q.append((starti,startj))
    visited[starti][startj] = True
    
    il = [-1,1,0,0]
    jl = [0,0,-1,1]
    
    while Q : 
        nodei,nodej = Q.popleft()
        visited[nodei][nodej] = True
        for c in range(4) :
            newi = nodei + il[c] 
            newj = nodej + jl[c] 
            
            if (0 <= newi <= N-1) and (0 <= newj <= N-1) and graph[newi][newj] > height:
                if not visited[newi][newj] :
                    visited[newi][newj] = True
                    Q.append((newi,newj))
    return +1
    

N = int(input())
graph = [list(map(int,input().split())) for y in range(N)]
visited = []


for i in range(1,101):
    visited = [[False for x in range(N)] for y in range(N)] 
    
    cnt = 0
    for j in range(0,N):
        for k in range(0,N):
            if graph[j][k] > i :
                cnt += bfs(j,k,i)
    if max < cnt :
        max = cnt

print(max)