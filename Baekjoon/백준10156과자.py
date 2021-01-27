if __name__ == '__main__' :
    x=input().split()

    price=int(x[0])*int(x[1]) #과자사기에 필요한 가격

    result=price-int(x[2]) #모자란 돈 계산
    if(result<=0): #가진 돈이 충분하면
        result=0

    print(result)