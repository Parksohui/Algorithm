if __name__=='__main__' :
    N=int(input())

    temp=len(str(N))-1 #일의 자리 수 빼고
    result=N #일의자리 수는 모든 수에 다 존재

    #십의 자리 수 = 전체 수 - 10 +1 에 다 존재
    #백의 자리 수 = 전체 수 - 100 +1 에 다 존재
    if temp!=0:
        n=1
        while(temp!=0):
            k=10**n
            result+=(N-k+1)
            n+=1
            temp-=1 #자리 수 빼기

    print(result)