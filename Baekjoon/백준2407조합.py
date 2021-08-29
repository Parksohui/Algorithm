import sys

if __name__=='__main__' :
    n,m=map(int,sys.stdin.readline().split())

    # n개의 원소의 m 조합) n!/(m!(n-m)!)

    nvalue=1
    for i in range(m+1,n+1): # n!/m!
        nvalue*=i

    mvalue=1
    for i in range(2,n-m+1): # (n-m)!
        mvalue*=i

    print(nvalue//mvalue) # n!/(m!(n-m)!)