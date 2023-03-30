l = ""
n = int(input())
for i in range(1,n+1):
    l += str(i)
for i in range(len(l)-len(str(n))+1):
    flag = 1
    for j in range(len(str(n))):
        if(l[i+j]!=str(n)[j]):
            flag =0
    if flag :
        print(i+1)
        break