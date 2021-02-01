if __name__=='__main__' :
    x=int(input())
    temp = int(input())

    while(temp):

        if temp%x ==0: #배수
            print(temp,"is a multiple of",x, end='')
            print(".")
        else:
            print(temp,"is NOT a multiple of",x,end='')
            print(".")


        temp = int(input())