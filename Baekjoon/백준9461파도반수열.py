if __name__=='__main__' :
    T=int(input())

    arr=[]
    for i in range(T): #입력
        x=int(input())
        arr.append(x)

    dp=[1,1,1,2,2,3,4,5]
    for i in range(8,max(arr)): #규칙
        dp.append(dp[i-1]+dp[i-5])

    for i in arr: #출력
        print(dp[i-1])
