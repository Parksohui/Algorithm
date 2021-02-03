if __name__=='__main__' :
    x=int(input())
    y=int(input())

    if x>0:
        if y>0: #제 1사분면
            print(1)
        else: #제 4사분면
            print(4)
    else:
        if y>0: #제 2사분면
            print(2)
        else: #제 3사분면
            print(3)