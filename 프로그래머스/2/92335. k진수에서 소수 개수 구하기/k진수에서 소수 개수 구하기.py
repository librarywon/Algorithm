import math

def is_primenum(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    s=""
    ss=""
    cnt = 0
    while n != 0:
        s += str(n%k)
        n = int(n/k)
        
    ln = len(s)
    for i in range(ln-1,-1,-1):
        if s[i] != '0':
            ss += s[i]
        else:
            if ss=="":
                continue
            if is_primenum(int(ss)):
                cnt +=1
                ss =""
            else:
                ss =""
                
    if ss=="":
        return cnt
    else:
        if is_primenum(int(ss)):
            cnt +=1
        return cnt