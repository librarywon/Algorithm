T = int(input())
l = [300,60,10]
p = []
for i in range(3):
    p.append(T//l[i])
    T = T%l[i]
if(T==0):
    for k in p:
        print(k,end=" ")
else:
    print(-1)