T = int(input())
l = [25,10,5,1]
for i in range(T):
    C = int(input())
    for k in l:
        print(C//k,end=" ")
        C = C%k
    print()