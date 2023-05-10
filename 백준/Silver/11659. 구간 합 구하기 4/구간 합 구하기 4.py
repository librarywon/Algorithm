import sys

input = sys.stdin.readline

N,Q= map(int,input().split())

A = [0]+list(map(int,input().split()))

prefix_sum = [0 for x in range(N+1)]
for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + A[i]

for i in range(Q):
    s, e = map(int, input().split())
    res = prefix_sum[e]-prefix_sum[s-1]
    print(res)