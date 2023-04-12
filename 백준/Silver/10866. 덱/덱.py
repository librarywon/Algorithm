import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
Q = deque()
size =0
for i in range(N):
    L = list(input().split())
    if L[0] == "push_back":
        Q.append(L[1])
        size+=1
    elif L[0] == "push_front":
        Q.appendleft(L[1])
        size+=1
    elif L[0] == "pop_back" :
        if size !=0:
            print(Q.pop())
            size -= 1
        else:
            print(-1)
    elif L[0] == "pop_front":
        if size != 0:
            print(Q.popleft())
            size -= 1
        else:
            print(-1)
    elif L[0] == "size" :
        print(size)
    elif L[0] == "back":
        if size !=0:
            print(Q[-1])
        else:
            print(-1)
    elif L[0] == "front":
        if size !=0:
            print(Q[0])
        else:
            print(-1)
    elif L[0] == "empty":
        if size == 0 :
            print(1)
        else:
            print(0)
