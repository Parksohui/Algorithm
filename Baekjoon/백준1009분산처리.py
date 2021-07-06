if __name__=='__main__':
    T=int(input())

    for i in range(T):
        a,b=input().split()

        result=1
        x=int(b)%4 #4자리씩 일의 자리가 반복됨
        if x==0: #나머지가 0이면 4로 나누어떨어짐
            k=4
        else:
            k=x
        for j in range(k):
            result*=int(a)

        temp=result%10 #10의 나머지
        if temp==0:
            print(10)
        else:
            print(temp)