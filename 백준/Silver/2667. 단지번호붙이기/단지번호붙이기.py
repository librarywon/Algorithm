from collections import deque
def bfs(starti, startj):
    Q = deque()  # 큐
    Q.append((starti, startj))
    visited[starti][startj] = True

    il = [-1, 1, 0, 0]
    jl = [0, 0, -1, 1]

    v = set()

    while Q:
        nodei, nodej = Q.popleft()
        v.add((nodei,nodej))
        visited[nodei][nodej] = True
        for c in range(4):
            newi = nodei + il[c]  # 각각 순서대로 -1,1,0,0
            newj = nodej + jl[c]  # 각각 순서대로 0,0,-1,1

            # 그리드 안에 있는가?
            if (0 <= newi <= N - 1) and (0 <= newj <= N - 1):
                # 방문하지 않았는가?
                if not visited[newi][newj]:
                    if graph[newi][newj] ==1 :
                        visited[newi][newj] = True
                        Q.append((newi, newj))

    return len(v)


N = int(input())
graph = [[int(x) for x in input()] for y in range(N)]
visited = [[False for x in range(N)] for y in range(N)]
cnt = 0
arr = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]==1:
            ret = bfs(i,j)
            cnt +=1
            arr.append(ret)
print(cnt)
arr.sort()
for num in arr:
    print(num)