import sys

input = sys.stdin.readline

N,K= map(int,input().split())
#수열 보관
A = [0]+list(map(int,input().split()))

#전처리 과정, prefix_sum list 만들기
window = sum(A[1:K+1])

res = window

for i in range(1,N-K+1):
    window -=A[i]
    window +=A[i+K]
    res = max(res,window)

print(res)
