def solution(msg):
    answer = []
    d = {}
    cnt = 1
    for i in range(ord('A'),ord('Z')+1):
        d[chr(i)] = cnt
        cnt +=1
        
    i=0
    s=""
    while i<len(msg):
        s += msg[i]
        if s in d:
            if i<len(msg)-1 and s+msg[i+1] in d:
                i+=1
                continue
            i+=1
            answer.append(d[s])
        else:
            d[s] =cnt
            cnt+=1
            s=""
            
    return answer