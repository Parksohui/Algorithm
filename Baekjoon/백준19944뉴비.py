if __name__=='__main__' :
    x=list(map(int,input().split()))

    N=x[0]
    M=x[1]

    if N>=M:
        if M<=2:
            print("NEWBIE!")
        else:
            print("OLDBIE!")
    else:
        print("TLE!")
