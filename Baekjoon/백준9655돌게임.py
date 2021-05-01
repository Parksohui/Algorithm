if __name__=='__main__':
    a=int(input())

    count=0
    while(a>0): #돌 1개 또는 3개 가져갈 수 있음
        count+=1
        if a>=3:
            a-=3
        else:
            a-=1

    if count%2==0:
        print("CY")
    else:
        print("SK")