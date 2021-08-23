import sys

if __name__=='__main__' :
    N=int(sys.stdin.readline().strip())

    arr=list(map(int,sys.stdin.readline().split()))

    cnt=0
    maxbig=1
    for i in range(N-1):
        if arr[i]<=arr[i+1]: #연속해서 커지는 경우
            cnt+=1
        else:
            if maxbig<cnt+1:
                maxbig=cnt+1
            cnt=0

    if cnt+1>maxbig: #마지막까지 연속해서 수열인 경우
        maxbig=cnt+1
        cnt=0

    for i in range(N-1): #연속해서 작아지는 경우
        if arr[i]>=arr[i+1]:
            cnt+=1
        else:
            if maxbig<cnt+1:
                maxbig=cnt+1
            cnt=0

    if cnt+1>maxbig: #마지막까지 연속해서 수열인 경우
        maxbig=cnt+1

    print(maxbig)