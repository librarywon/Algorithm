import sys, math
def find_num(a,num):
    top=0
    tail=len(a)-1

    if top==tail:
        return int((num in a))
    while tail-top >0:
        if a[math.floor((top+tail)/2)] == num:
            return 1
        elif tail-top<=1 :
            if a[math.floor((top+tail)/2)+1] == num:
                return 1
            else:
                return 0
        elif a[math.floor((top+tail)/2)] < num:
            top = math.floor((top+tail)/2)
        elif a[math.floor((top+tail)/2)] > num:
            tail = math.floor((top+tail)/2)
a_num =int(sys.stdin.readline())
a =[]
a = list(map(int,sys.stdin.readline().split()))
b_num =int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
a.sort()
for i in b:
    print(find_num(a,i))