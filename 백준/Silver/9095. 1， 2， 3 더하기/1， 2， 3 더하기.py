import sys

input = sys.stdin.readline

from collections import defaultdict
D = defaultdict(int)

N = int(input())

D[1] = 1
D[2] = 2
D[3] = 4


for j in range(N):
    n = int(input())
    for i in range(4,n+1):
        D[i] = D[i-1] + D[i-2] + D[i-3]
    print(D[n])