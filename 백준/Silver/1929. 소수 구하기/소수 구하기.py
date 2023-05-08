MAX = 10**6
isPrime = [True for x in range(MAX+1)]
isPrime[0],isPrime[1] = False, False
for i in range(2,int(MAX**0.5)+1):
    if isPrime[i]:
        for k in range(i*2,MAX+1,i):
            isPrime[k] = False
M,N = map(int,input().split())
for i in range(M,N+1):
    if isPrime[i]:
        print(i)