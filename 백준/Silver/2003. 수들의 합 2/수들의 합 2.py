import sys

input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
s=0;e=1;sum=A[0]
res=0
while s != N:
    if M > sum:
        if e==N:
            break
        sum +=A[e]
        e+=1
    if M < sum:
        sum -=A[s]
        s+=1
    if M == sum:
        res +=1
        if e == N:
            break
        sum += A[e]
        e += 1
print(res)