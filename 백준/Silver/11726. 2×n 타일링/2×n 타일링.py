import sys
input = sys.stdin.readline
from collections import defaultdict

D = defaultdict(int)

D[1] = 1
D[2] = 2

n = int(input())

for i in range(3,n+1):
    D[i] = D[i-1] + D[i-2]

print(D[n]%10007)