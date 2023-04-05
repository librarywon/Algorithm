min = 99999999
N,M = map(int,input().split())
B = []
for i in range(N):
    B.append(input())
for i in range(N-7):
    for j in range(M-7):
        if(B[i][j] == 'W'):
            empty = 0
            for k in range(i,i+8):
                for q in range(j,j+8):
                    if((k-i)%2==0 and (q-j)%2==0 and B[k][q] !="W"):
                        empty+=1
                    elif ((k-i)%2==0 and (q-j)%2==1 and B[k][q] !="B"):
                        empty+=1
                    elif ((k-i)%2==1 and (q-j)%2==0 and B[k][q] !="B"):
                        empty+=1
                    elif ((k-i)%2==1 and (q-j)%2==1 and B[k][q] !="W"):
                        empty+=1
            if (empty < min):
                min = empty
            empty = 0
            for k in range(i, i + 8):
                for q in range(j, j + 8):
                    if ((k - i) % 2 == 0 and (q - j) % 2 == 0 and B[k][q] != "B"):
                        empty += 1
                    elif ((k - i) % 2 == 0 and (q - j) % 2 == 1 and B[k][q] != "W"):
                        empty += 1
                    elif ((k - i) % 2 == 1 and (q - j) % 2 == 0 and B[k][q] != "W"):
                        empty += 1
                    elif ((k - i) % 2 == 1 and (q - j) % 2 == 1 and B[k][q] != "B"):
                        empty += 1
            if (empty < min):
                min = empty
        else:
            empty = 0
            for k in range(i, i + 8):
                for q in range(j, j + 8):
                    if((k-i)%2==0 and (q-j)%2==0 and B[k][q] !="B"):
                        empty+=1
                    elif ((k-i)%2==0 and (q-j)%2==1 and B[k][q] !="W"):
                        empty+=1
                    elif ((k-i)%2==1 and (q-j)%2==0 and B[k][q] !="W"):
                        empty+=1
                    elif ((k-i)%2==1 and (q-j)%2==1 and B[k][q] !="B"):
                        empty+=1
            if (empty < min):
                min = empty
            empty = 0
            for k in range(i, i + 8):
                for q in range(j, j + 8):
                    if ((k - i) % 2 == 0 and (q - j) % 2 == 0 and B[k][q] != "W"):
                        empty += 1
                    elif ((k - i) % 2 == 0 and (q - j) % 2 == 1 and B[k][q] != "B"):
                        empty += 1
                    elif ((k - i) % 2 == 1 and (q - j) % 2 == 0 and B[k][q] != "B"):
                        empty += 1
                    elif ((k - i) % 2 == 1 and (q - j) % 2 == 1 and B[k][q] != "W"):
                        empty += 1
            if (empty < min):
                min = empty

if(min==99999999):
    print(0)
else:
    print(min)