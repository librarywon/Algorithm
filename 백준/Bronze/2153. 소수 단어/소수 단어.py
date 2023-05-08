#1도 소수로 판명 A 65, a 97
def isPrime(num):
    if num == 1 or num==2:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
word = input()
sum = 0
for w in word:
    if w >= 'a':
        sum += ord(w) -96
    elif w < 'a':
        sum += ord(w) -38

if(isPrime(sum)):
    print("It is a prime word.")
else:
    print("It is not a prime word.")