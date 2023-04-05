n = int(input())
l = []
for i in range(n):
    s = input()
    num = 0
    for k in s:
        if('0'<= k <='9'):
            num += int(k)
    l.append([s,num])
l.sort(key=lambda x : (len(x[0]),x[1],x[0]))
for k in l:
    print(k[0])