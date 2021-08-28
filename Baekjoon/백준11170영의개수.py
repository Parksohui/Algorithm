import sys

if __name__=='__main__' :
    T=int(sys.stdin.readline().strip())

    for i in range(T):
        x=list(map(int,sys.stdin.readline().split()))

        cnt=0
        for j in range(x[0],x[1]+1):
            cnt+=str(j).count('0') #0의 개수

        print(cnt)
