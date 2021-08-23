if __name__=='__main__' :
    M,N=map(int,input().split())
    
    #소수 구하기
    arr=[True]*(N+1)
    line=int((N+1)*0.5)
    for i in range(2,line+1):
        if arr[i]==True:
            for j in range(i+i,N+1,i):
                arr[j]=False
    
    #소수 판별
    for i in range(M,N+1):
        if i==1: #1은 소수가 아님
            pass
        elif arr[i]==True:
            print(i)
