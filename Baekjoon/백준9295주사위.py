if __name__=='__main__' :
    T=int(input())

    for i in range(T):
        x=list(map(int,input().split()))

        print("Case %d: %d"%(i+1,sum(x)))