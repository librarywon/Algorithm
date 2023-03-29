from collections import defaultdict
S1,S2,S3 = map(int,input().split())
D = defaultdict(int)
for i in range(S1):
    for j in range(S2):
        for k in range(S3):
            D[i+j+k+3] +=1
m = max(D.values())
res = []
for k,v in D.items():
    if v==m:
        res.append(k)
res.sort()
print(res[0])