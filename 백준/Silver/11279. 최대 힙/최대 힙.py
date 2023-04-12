import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for i in range(N):
    n = int(input())
    if n !=0:
        heapq.heappush(heap,-1*n)
    else:
        if heap :
            print(heapq.heappop(heap)*-1)
        else:
            print(0)