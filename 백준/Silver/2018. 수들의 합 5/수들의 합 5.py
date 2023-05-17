import sys
input = sys.stdin.readline
N = int(input())
#수열 보관
A = [x for x in range(N+1)]
#초기 설정 만져줌
s=0;e=1;sum=A[0]
res=1
while s != N:
    #작을 때 뒤에 숫자를 더함
    if N > sum:
        if e==N:
            break
        sum +=A[e]
        e+=1
    #클 때 앞에 숫자를 빼 줌
    if N < sum:
        sum -=A[s]
        s+=1
    #같을 때 res를 1늘리고 뒷 숫자를 더 함
    if N == sum:
        res +=1
        if e == N:
            break
        sum += A[e]
        e += 1
print(res)