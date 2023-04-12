import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
for i in range(N):
    S = []
    flag = True
    vps = input().strip()
    for k in vps:
        if S :
            if k == ")" :
                S.pop()
            else:
                S.append(k)
        else :
            if k==")":
                flag = False
                break
            else:
                S.append(k)

    if flag and len(S) == 0 :
        print("YES")
    else:
        print("NO")