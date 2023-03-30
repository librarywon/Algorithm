string = input()
tar = input()
cnt = 0
S=len(string)
T=len(tar)
i=0
while(i<S-T+1):
    flag = True
    for j in range(T):
        if string[i+j] != tar[j]:
            flag = False
            break
    if flag :
        cnt +=1
        i += len(tar)
    else:
        i +=1
print(cnt)