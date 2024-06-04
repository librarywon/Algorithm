def cal_diff(h1, m1, h2, m2):
    return (h2 * 60 + m2) - (h1 * 60 + m1)

def add_minutes(h, m, minutes):
    total_minutes = h * 60 + m + minutes
    return total_minutes // 60, total_minutes % 60

def solution(plans):
    answer = []
    wait = []
    
    # plans를 시작 시간으로 정렬
    plans = sorted(plans, key=lambda x: x[1])
    nplans = []

    for r, t, c in plans:
        h, m = map(int, t.split(":"))
        nplans.append([r, h, m, int(c)])
    
    current_task, ch, cm, ctime = nplans[0]
    
    for k in range(1, len(nplans)):
        next_task, nh, nm, ntime = nplans[k]
        time_diff = cal_diff(ch, cm, nh, nm)
        
        if time_diff < ctime:
            wait.append([current_task, ctime - time_diff])
        else:
            answer.append(current_task)
            extra_time = time_diff - ctime
            ch, cm = add_minutes(ch, cm, ctime)
            
            while extra_time > 0 and wait:
                wait_task, wait_time = wait.pop()
                if extra_time >= wait_time:
                    answer.append(wait_task)
                    ch, cm = add_minutes(ch, cm, wait_time)
                    extra_time -= wait_time
                else:
                    wait.append([wait_task, wait_time - extra_time])
                    ch, cm = add_minutes(ch, cm, extra_time)
                    extra_time = 0
            
        current_task, ch, cm, ctime = next_task, nh, nm, ntime
    
    answer.append(current_task)
    ch, cm = add_minutes(ch, cm, ctime)
    
    while wait:
        wait_task, wait_time = wait.pop()
        answer.append(wait_task)    
    
    return answer
