if __name__=='__main__':
    L=int(input())
    A=int(input())
    B=int(input())

    C=int(input())
    D=int(input())

    #방학숙제 최대 날의 수
    max=A//C

    if(A%C !=0):
        max+=1
    temp=B//D

    if(B%D !=0):
        temp+=1

    if(max< temp ):
        max=temp

    print(L-max)