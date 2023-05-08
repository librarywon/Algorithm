import math
def isPrime(num):
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
count = 0
input()
for i in map(int,input().split()):
    if(isPrime(i)):
        count +=1
print(count)