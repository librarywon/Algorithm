def solution(n, left, right):
    answer = []
    l = []
    ly = left // n
    lx = left % n
    ry = right // n
    rx = right % n
    
    if ly == ry :
        for i in range(ly+1):
            l.append(ly+1)
        for i in range(ly+2,n+1):
            l.append(i)
        return l[lx:rx+1]
    else:
        for i in range(ly+1,ry+2):
            for k in range(i):
                l.append(i)
            for j in range(i+1,n+1):
                l.append(j)
        return l[lx:rx+(ry-ly)*n+1]