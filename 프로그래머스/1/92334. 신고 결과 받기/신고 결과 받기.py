def solution(id_list, report, k):
    answer = []
    re_s = []
    for i in range(len(id_list)):
        re_s.append([])
        answer.append(0)
        
    for s in report:
        u1, u2 = s.split()
        u1_ind = id_list.index(u1)
        u2_ind = id_list.index(u2)
                
        if u1_ind not in re_s[u2_ind]:
            re_s[u2_ind].append(u1_ind)
            
    for l in re_s:
        if len(l) >= k:
            for a in l:
                answer[a] +=1
                
    return answer