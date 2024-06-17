def find_index(n):
    for i in range(5):
        for j in range(5):
            if pan[i][j] == n:
                return i, j


row = [5, 5, 5, 5, 5]
col = [5, 5, 5, 5, 5]
cro = [5, 5]

pan = []
call = []
cnt = 0
bingo = 0
for i in range(5):
    pan.append(input().split())

for i in range(5):
    call.append(input().split())

for l in call:
    for n in l:
        cnt += 1
        r, c = find_index(n)

        if r == 2 and c == 2:
            cro[0] -= 1
            cro[1] -= 1
            row[r] -= 1
            col[c] -= 1
        elif r == c:
            cro[0] -= 1
            row[r] -= 1
            col[c] -= 1
        elif (r == 0 and c== 4) or (r == 1 and c== 3) or (r == 3 and c== 1) or (r == 4 and c== 0):
            cro[1] -=1
            row[r] -= 1
            col[c] -= 1
        else:
            row[r] -= 1
            col[c] -= 1

        if row[r] == 0 :
            row[r] = -1
            bingo += 1

        if col[c] == 0 :
            col[c] = -1
            bingo +=1

        if cro[0] == 0 :
            cro[0] = -1
            bingo += 1

        if cro[1] == 0 :
            cro[1] = -1
            bingo += 1

        if bingo >= 3:
            print(cnt)
            break
    if bingo >= 3:
        break