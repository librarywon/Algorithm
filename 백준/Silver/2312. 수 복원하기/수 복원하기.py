from collections import defaultdict
N= 10**6
isPrime = [True for x in range(N+1)]
isPrime[0],isPrime[1]= False,False

for i in range(2,int(N**0.5)+1):
    if isPrime[i]:
        for j in range(i*2,N+1,i):
            isPrime[j] = False
Primes = []
for i in range(2,N+1):
    if isPrime[i]:
        Primes.append(i)
num =int(input())

for i in range(num):
    n = int(input())
    res = defaultdict(int)
    for prime in Primes:
        while n%prime==0:
            n//=prime
            res[prime] +=1
    for k,v in res.items():
        print(k,v)

