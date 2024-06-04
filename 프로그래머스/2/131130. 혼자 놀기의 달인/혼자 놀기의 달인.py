def solution(cards):
    answer = 0
    n = len(cards)
    v = [0] * n
    box = []
    for i in range(n):
        p = i
        cnt = 0
        if v[i] == 0:
            while 1:
                if v[p] == 1:
                    box.append(cnt)
                    break
                else:
                    cnt +=1
                    v[p] = 1
                    p=cards[p]-1
    box = sorted(box,reverse=True)
    
    if len(box) <=1 :
        return 0
    else:
        return box[0]*box[1]