if __name__=='__main__' :
    N=int(input())

    bol=False
    for i in range(31):
        temp=2**i

        if temp==N: #제곱수이면
            bol=True
            break

    if bol==True:
        print(1)
    else:
        print(0)
