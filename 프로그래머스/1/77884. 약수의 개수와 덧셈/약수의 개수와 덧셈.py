def count_div(n):
    if n == 1 :
        return 1
    
    cnt = 2
    for i in range(2,n):
        if(n%i == 0):
            cnt+=1
            
    return cnt

def solution(left, right):
    answer = 0
    if left == right :
        return left
    
    for i in range(left,right+1):
        n = count_div(i)
        if (n%2==0) :
            answer +=i
        else:
            answer -=i
            
    return answer