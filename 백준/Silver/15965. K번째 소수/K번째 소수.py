N= 5*10**5
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
print(Primes[num-1])