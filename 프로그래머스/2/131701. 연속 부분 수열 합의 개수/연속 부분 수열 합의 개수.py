def solution(elements):
    answer = 0
    set_nums = set()
    n = len(elements)
    for i in range(0,n):
        acc_sum = 0
        for j in range(0,n):
            acc_sum += elements[j]
            set_nums.add(acc_sum)
        elements = [elements.pop()] + elements
    
    return len(set_nums)