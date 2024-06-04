def solution(cards):
    answer = 0
    same = 0
    for i in range(0,len(cards)):
        if(cards[i]== i+1):
            same +=1
            
    r = len(cards)-same
    
    if r%2==0:
        answer = int(r/2) ** 2
    else:
        answer = int(r/2) * (int(r/2)+1)
        
    if r==0 :
        answer = 1
    
    return answer