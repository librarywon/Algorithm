def solution(cacheSize, cities):
    answer = 0
    buf = []
    
    for city in cities :
        city = city.upper()
        if city in buf:
            buf.remove(city)   
            buf.append(city)
            answer +=1
        else:
            if(cacheSize >0):
                if(len(buf)==cacheSize):
                    del buf[0]
                buf.append(city)
            answer +=5
        
    return answer