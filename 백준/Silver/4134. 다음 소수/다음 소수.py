def isPrime(num):
    if num ==1 or num==0:
        return False
    if num ==2 :
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(int(input())):
    num = int(input())
    while 1:
        if isPrime(num):
            print(num)
            break
        else:
            num +=1