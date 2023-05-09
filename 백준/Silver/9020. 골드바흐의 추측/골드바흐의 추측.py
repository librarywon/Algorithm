N= 10**4
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
    res=[]
    for prime in Primes:
        if n < prime:
            break
        if n-prime in Primes:
            res.append([prime,n-prime])
    min_n1 =res[0][0]
    min_n2 =res[0][1]
    for n1,n2 in res:
        if abs(min_n1-min_n2) > abs(n1-n2):
            min_n1 = n1
            min_n2 = n2
    print(min_n1,min_n2)