if __name__=='__main__' :
    x=int(input())
    temp=2

    while x!=1:
        if x%temp==0:
            x=x/temp
            print(temp)
        else:
            temp+=1