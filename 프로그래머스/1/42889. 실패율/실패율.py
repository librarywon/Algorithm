def solution(N, stages):
    answer = {}
    people = len(stages)
    fail = {}

    for i in range(1, N+1):
        if(people != 0):
            count = stages.count(i)
            fail[i] = count / people
            people -= count
        else :
            fail[i] = 0

    answer = sorted(fail, key=lambda i:fail[i], reverse=True)

    return answer 