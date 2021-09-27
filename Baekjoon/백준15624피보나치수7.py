import sys
if __name__=='__main__':
    n=int(sys.stdin.readline().strip())

    if n==0: #0일때
        print(0)
    elif n==1: #1일때
        print(1)
    else: #n일때
        a,b=0,1
        for i in range(2, n+1):
            x=(a+b)%1000000007
            a=b
            b=x
        print(b)


