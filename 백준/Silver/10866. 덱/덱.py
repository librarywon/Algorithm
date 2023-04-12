import sys
num =int(sys.stdin.readline())
a=[0]*10000
cnt=0
for i in range(num):
    word = sys.stdin.readline().split()
    if word[0]=="push_front":
        for i in range(cnt-1,-1,-1):
            a[i+1] = a[i]
        a[0]= int(word[1])
        cnt +=1
    if word[0]=="push_back":
        a[cnt]= int(word[1])
        cnt +=1
    if word[0]=="pop_front":
        if cnt==0:
            print(-1)
        elif cnt==1:
            print(a[0])
            a[0]==0
            cnt-=1
        else:
            print(a[0])
            for i in range(cnt):
                if i+1 !=cnt:
                    a[i] = a[i+1]
            a[cnt-1]=0
            cnt-=1
    if word[0] == "pop_back":
        if cnt==0:
            print(-1)
        else:
            print(a[cnt-1])
            cnt-=1
            a.pop()
    if word[0]=="size":
        print(cnt)
    if word[0]=="empty":
        if cnt == 0:
            print(1)
        else:
            print(0)
    if word[0] == "front":
        if cnt==0:
            print(-1)
        else:
            print(a[0])
    if word[0] == "back":
        if cnt==0:
            print(-1)
        else:
            print(a[cnt-1])
