def solution(k, tangerine):
    answer = 0
    d = {}
    for s in tangerine:
        if s in d:
            d[s] +=1
        else:
            d[s] = 1
            
    sl = 0
    
    #정렬된 귤 크기별 갯수 기준으로 내림차순 리스트
    for c in sorted(d.values(),reverse=True):
        if sl >= k:
            break
        sl += c
        answer +=1
    
    return answer