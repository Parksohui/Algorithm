if __name__=='__main__':
    x=list(map(int,input().split())) #입력

    case=0
    while(x[0]!=0): #입력 종료 조건: L,P,V=0
        sum=0
        case+=1
        div=x[2]//x[1] #몫
        sum+=div*x[0] 
        if x[2]%x[1] >= x[0]: #L일만
            sum+=x[0]
        else: #나머지가 L보다 작을 경우
            sum+=x[2]%x[1]

        print("Case "+str(case)+": "+str(sum)) #출력
        x = list(map(int, input().split())) #입력
