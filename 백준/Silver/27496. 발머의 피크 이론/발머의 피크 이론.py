import sys
input = sys.stdin.readline
N,K = map(float,(input().split()))
A = [0]+list(map(float,input().split()))
A_new = [i * 0.001 for i in A]
#1~k까지의 합 구성
cnt = 0
front =1
back=1
window = 0
while(front != N+1):
    if(front<=K):
        window += A_new[front]
        front +=1
    else:
        window -=A_new[back]
        window +=A_new[front]
        front +=1
        back +=1
    if 0.129 <= round(window,5) <= 0.138:
        cnt += 1
print(cnt)