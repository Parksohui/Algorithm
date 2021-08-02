if __name__=='__main__' :
    a,b=input().split()

    #set 사용
    A=set(map(int,input().split()))
    B=set(map(int,input().split()))

    print(len(A-B)+len(B-A))