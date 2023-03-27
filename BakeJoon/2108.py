import sys
from collections import defaultdict
input = sys.stdin.readline #이거 때문에 그랬음
n =int(input())
list = []
D = defaultdict(int)
for i in range(n):
    N = int(input())
    D[N]+=1
    list.append(N)
list.sort()
print(int('{:.0f}'.format(sum(list)/n)))
print(list[int(n/2)])
list2=[]
many = max(D.values())
for k,v in D.items():
    if many == v:
        list2.append(k)
list2.sort()
if len(list2)>1:
    print(list2[1])
else:
    print(list2[0])
print(list[n-1]-list[0])